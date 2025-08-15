from PySide6.QtWidgets import QDialog, QTableWidget, QVBoxLayout, QLabel, QHeaderView, QAbstractItemView
from PySide6.QtCore import Qt
from PySide6.QtGui import QFontMetrics

class SpecsWindow(QDialog):
    def __init__(self, specs_dict, parent=None, typeSpecs="Характеристики товара"):
        super().__init__(parent)
        self.setWindowTitle(typeSpecs)
        self.resize(900, 600)

        layout = QVBoxLayout(self)
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Характеристика", "Значение"])

        # Запрет изменения размеров пользователем
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        

        # Первый столбец фиксированной ширины, второй растягивается
        self.table.setColumnWidth(0, 300)
        self.table.horizontalHeader().setStretchLastSection(True)

        # Убираем горизонтальный скролл, чтобы перенос работал предсказуемо
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Заполнение
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)

        for key, value in specs_dict.items():
            r = self.table.rowCount()
            self.table.insertRow(r)

            key_lbl = QLabel(key)
            key_lbl.setWordWrap(True)
            key_lbl.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            key_lbl.setTextInteractionFlags(Qt.NoTextInteraction)  # нельзя выделять

            val_lbl = QLabel(value)
            val_lbl.setWordWrap(True)
            val_lbl.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            val_lbl.setTextInteractionFlags(Qt.TextSelectableByMouse)  # можно копировать

            self.table.setCellWidget(r, 0, key_lbl)
            self.table.setCellWidget(r, 1, val_lbl)

            # Фиксируем высоту строки по содержимому (важно при Fixed)
            h = max(key_lbl.sizeHint().height(), val_lbl.sizeHint().height())
            self.table.setRowHeight(r, h)

        # Можно оставить сортировку выключенной, чтобы не было артефактов с widget'ами
        # self.table.setSortingEnabled(True)

        layout.addWidget(self.table)

    # Если хочешь, чтобы при ресайзе окна высоты пересчитывались (изменяется ширина → перенос):
    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Пересчитать высоты строк под новую ширину
        for r in range(self.table.rowCount()):
            w0 = self.table.columnWidth(0)
            w1 = self.table.viewport().width() - w0  # примерная ширина второй колонки
            key_lbl = self.table.cellWidget(r, 0)
            val_lbl = self.table.cellWidget(r, 1)
            if key_lbl and val_lbl:
                # Обновляем sizeHint через временное ограничение ширины
                key_lbl.setFixedWidth(w0 - 8)
                val_lbl.setFixedWidth(max(0, w1 - 8))
                h = max(key_lbl.sizeHint().height(), val_lbl.sizeHint().height())
                self.table.setRowHeight(r, h)
                key_lbl.setFixedWidth(16777215)
                val_lbl.setFixedWidth(16777215)
