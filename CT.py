import sys
from PyQt5.QtWidgets import *

from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtWidgets

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
        # layout.addRow(li, lil)
        self.layout.addRow(self.sun, self.sunl)

        self.button1 = QPushButton(self.win)
        self.button1.setText("UPLOAD PDF")
        self.layout.addRow(self.button1)

        self.button = QPushButton(self.win)
        self.button.setText("SUBMIT")
        self.layout.addRow(self.button)
        self.button1.clicked.connect(self.open)
        self.button.clicked.connect(self.save)
        self.setWindowTitle("UPLOAD PDF")
        self.setGeometry(100, 100, 320, 200)
        self.setLayout(self.layout)

    def open(self, name):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, self._ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                            "All Files (*);;Python Files (*.py)", options=options)
        if self.fileName:
            return self.fileName

    # file = open.fileName

    def save(self):
        if createConnection():
            name = self.Nl.text()
            stream_name = self.snl.text()
            sub_name = self.sunl.text()
            file = self.fileName
            print(name, stream_name, sub_name, file)
            self.win.close()


class search(QWidget):
    def __init__(self):
        super().__init__()
        lay = QtWidgets.QVBoxLayout(self)
        lineEdit = QtWidgets.QLineEdit()
        tableView = QtWidgets.QTableView()
        lay.addWidget(lineEdit)
        lay.addWidget(tableView)


class Home(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()

        button1 = QPushButton(widget)
        button1.setText("UPLOAD PDF")
        button1.move(87, 32)
        button1.clicked.connect(self.button1_clicked)

        # self.button2 = QPushButton(widget)
        # self.button2.setText("SEARCH PDF")
        # self.button2.move(87, 64)
        # self.button2.clicked.connect(self.button2_clicked)

        widget.setGeometry(50, 50, 320, 200)
        widget.setWindowTitle("ADMIN PDF SYSTEM")
        widget.show()
        sys.exit(app.exec_())

    def button1_clicked(self):
        self.w = upload()
        self.w.show()

    # def button2_clicked(self):
    #     self.s = search()
    #     self.s.show()


app = QApplication(sys.argv)
window = upload()
window.show()
app.exec_()
