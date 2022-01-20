import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('database.sqlite')
        db.open()

        view = QTableView(self)
        model = QSqlTableModel(self, db)
        model.setTable('RECORDS')
        model.select()

        view.setModel(model)
        view.move(10, 10)
        view.resize(430, 315)
        view.setEnabled(0)


        self.setGeometry(300, 100, 450, 335)
        self.setWindowTitle('Leaderboard')







