from PySide6.QtWidgets import QApplication, QMainWindow
from ui_CompInfoWindow import Ui_CompInfo
import requests
import textwrap
from functools import partial
import re
from bs4 import BeautifulSoup

class CompInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CompInfo()
        self.ui.setupUi(self)

        self.mapping = [
            (self.ui.pushButton_3,  self.ui.textEdit,    self.ui.textEdit_13, self.ui.label_13),
            (self.ui.pushButton_4,  self.ui.textEdit_2,  self.ui.textEdit_14, self.ui.label_14),
            (self.ui.pushButton_5,  self.ui.textEdit_3,  self.ui.textEdit_15, self.ui.label_15),
            (self.ui.pushButton_6,  self.ui.textEdit_4,  self.ui.textEdit_16, self.ui.label_16),
            (self.ui.pushButton_7,  self.ui.textEdit_5,  self.ui.textEdit_17, self.ui.label_17),
            (self.ui.pushButton_8,  self.ui.textEdit_6,  self.ui.textEdit_18, self.ui.label_18),
            (self.ui.pushButton_9,  self.ui.textEdit_7,  self.ui.textEdit_19, self.ui.label_19),
            (self.ui.pushButton_10, self.ui.textEdit_8,  self.ui.textEdit_20, self.ui.label_20),
            (self.ui.pushButton_11, self.ui.textEdit_9,  self.ui.textEdit_21, self.ui.label_21),
            (self.ui.pushButton_12, self.ui.textEdit_10, self.ui.textEdit_22, self.ui.label_22),
            (self.ui.pushButton_13, self.ui.textEdit_11, self.ui.textEdit_23, self.ui.label_23),
            (self.ui.pushButton_14, self.ui.textEdit_12, self.ui.textEdit_24, self.ui.label_24),
        ]

        self.output_edits = [out for _, _, out, _ in self.mapping]

        for button, input_edit, output_edit, label in self.mapping:
            button.clicked.connect(partial(self.update_info, input_edit, output_edit, label))

    def get_specs_from_html(self, product_url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        
        response = requests.get(product_url, headers=headers, timeout=10)
        response.raise_for_status()
            
        soup = BeautifulSoup(response.text, "html.parser")
            
            # Инициализируем словарь для характеристик
        specs_dict = {}
            
            # Парсим основные характеристики (новый стиль Onliner)
        for spec in soup.select(".product-specs__table tr:not(.product-specs__table-title)"):
            name = spec.select_one("td").get_text(" ", strip=True)

            value_cell = spec.select_one("td + td")  # второй столбец
            value = None

            if value_cell:
                # Пробуем сначала текст
                text_value = value_cell.select_one(".value__text")
                if text_value:
                    value = ' '.join(text_value.get_text(" ", strip=True).split())
                else:
                    # Если текста нет, проверяем иконки
                    if value_cell.select_one(".i-tip"):
                        value = "Да"
                    elif value_cell.select_one(".i-x"):
                        value = "Нет"

            if name and value:
                specs_dict[name] = value

                
        return specs_dict


    def get_product_info(self, product_url):
        product_code = product_url.rstrip("/").split("/")[-1]
        api_url = f"https://catalog.onliner.by/sdapi/catalog.api/products/{product_code}"
        specs_url = f"https://catalog.onliner.by/sdapi/catalog.api/products/{product_code}/specs"

        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        #print(data)

        name = data.get("full_name") or data.get("name") or "Без названия"

        try:
            price_amount = data["prices"]["price_min"]["amount"]
            price = float(price_amount)
        except (KeyError, TypeError, ValueError):
            price = 0.0


        print(self.get_specs_from_html(product_url))

        return name, price

    def update_info(self, input_edit, output_edit, label):
        name, price = self.get_product_info(input_edit.toPlainText())
        label.setText(name)

        html_template = textwrap.dedent(f"""\
        <html><body style="font-family:'Segoe UI'; font-size:9pt;">
        <p align="center"><span style="font-size:14pt; color:#ff0000;">{price:.2f} BYN</span></p>
        </body></html>
        """)
        output_edit.setHtml(html_template)

        self.recalculate_total_from_fields()

    def _extract_price(self, text: str) -> float:
        m = re.search(r'(\d[\d\s]*[.,]?\d*)', text)
        if not m:
            return 0.0
        s = m.group(1).replace(' ', '').replace(',', '.')
        try:
            return float(s)
        except ValueError:
            return 0.0

    def recalculate_total_from_fields(self):
        total = 0.0
        for edit in self.output_edits:
            total += self._extract_price(edit.toPlainText())
        self.ui.label_25.setText(f"Итого: {total:.2f} BYN")


if __name__ == "__main__":
    app = QApplication([])
    window = CompInfo()
    window.show()
    app.exec()
