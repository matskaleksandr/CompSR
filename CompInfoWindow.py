from PySide6.QtWidgets import QApplication, QMainWindow
from ui_CompInfoWindow import Ui_CompInfo
from PySide6.QtGui import QTextCursor
import requests
import textwrap
from functools import partial

class CompInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CompInfo()
        self.ui.setupUi(self)

        # Список кнопок с их соответствующими полями ввода/вывода
        mapping = [
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

        # Подключаем кнопки к универсальному обработчику
        for button, input_edit, output_edit, label in mapping:
            button.clicked.connect(partial(self.update_info, input_edit, output_edit, label))

    def get_product_info(self, product_url):
        product_code = product_url.rstrip("/").split("/")[-1]
        api_url = f"https://catalog.onliner.by/sdapi/catalog.api/products/{product_code}"
        
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        name = data.get("full_name") or data.get("name") or "Без названия"
        
        try:
            price_amount = data["prices"]["price_min"]["amount"]
            price = str(float(price_amount))
        except (KeyError, TypeError):
            price = "0"
        
        return name, price

    def update_info(self, input_edit, output_edit, label):
        name, price = self.get_product_info(input_edit.toPlainText())
        label.setText(name)

        cursor = output_edit.textCursor()
        cursor.select(QTextCursor.Document)

        html_template = textwrap.dedent(f"""\
        <html><body style="font-family:'Segoe UI'; font-size:9pt;">
        <p align="center"><span style="font-size:14pt; color:#ff0000;">{price}</span></p>
        </body></html>
        """)
        cursor.insertHtml(html_template)

if __name__ == "__main__":
    app = QApplication([])
    window = CompInfo()
    window.show()
    app.exec()
