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



class upload(QWidget):
    def __init__(self):
        super().__init__()
        self.win = QWidget()

        self.layout = QFormLayout()

        self.Name = QLabel("Your Name")
        self.Nl = QLineEdit()

        self.sn = QLabel("Stream Name")
        self.snl = QLineEdit()
        self.snl.setToolTip("<h3>MBBS, DENTAL ... </h3>")
        self.li = QLabel("Lecture ID")
        self.lil = QLineEdit()
        self.lil.setToolTip("<h3>1_12345</h3>")
        self.sun = QLabel("Subject Name")
        self.sunl = QLineEdit()
        self.sunl.setToolTip("<h3>Anatomy, Gynecology ..</h3>")

        self.layout.addRow(self.Name, self.Nl)
        self.layout.addRow(self.sn, self.snl)
        self.layout.addRow(self.li, self.lil)
        self.layout.addRow(self.sun, self.sunl)

        self.button1= QPushButton(self.win )
        self.button1.setText("UPLOAD PDF")
        self.layout.addRow(self.button1)

        self.button2 = QPushButton(self.win )
        self.button2.setText("SUBMIT")
        self.layout.addRow(self.button2)
        self.button1.clicked.connect(self.open)
        self.button2.clicked.connect(self.submit)
        self.setWindowTitle("UPLOAD PDF")
        self.setGeometry(100, 100, 320, 200)
        self.setLayout(self.layout)

    def open(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '', 'All Files (*.*)')
        if path != ('', ''):
            print("File path : " + path[0])

    def submit(self):
        print("submitted ")


app = QApplication(sys.argv)
window = upload()
window.show()
app.exec_()
