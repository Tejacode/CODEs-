import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

from PyQt5.QtSql import *


SERVER = 'MEDISYS-SOFT5\SQLEXPRESS,49677'
DATABASE = 'userdb'
USERNAME = 'teja'
PASSWORD = '7799'


def createConnection():
    connString = f'DRIVER={{SQL Server}};' \
                 f'SERVER={SERVER};' \
                 f'DATABASE={DATABASE}'

    global db
    db = QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(connString)

    if db.open():
        print('connect to SQL Server successfully')
        return True
    else:
        print('connection failed')
        return False


class search(QWidget,):
    def __init__(self):
        super().__init__()
        self.lay = QtWidgets.QVBoxLayout(self)
        self.lineEdit = QtWidgets.QLineEdit()
        self.tableView = QtWidgets.QTableView()
     #   ans = lineEdit.text()

        self.searchb = QtWidgets.QPushButton("Search")
        self.lable = QLabel(self)

        self.lineEdit.returnPressed.connect(self.getans)
        self.searchb.clicked.connect(self.getans)

        self.lay.addWidget(self.lineEdit)
        self.lay.addWidget(self.searchb)
        #self.lay.addWidget(self.tableView)
        self.lay.addWidget(self.lable)
        #searchb.clicked.connect(self.getans)

    def getans(self):
        self.lable.setText(self.lineEdit.text())




app = QApplication(sys.argv)
window = search()
window.show()
app.exec_()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     if createConnection():
#         SQL_STATEMENT = 'SELECT * FROM dbo.sportsmen'
#         dataView = search(SQL_STATEMENT)
#         dataView.show()
#
#     app.exit()
#     sys.exit(app.exec_())

