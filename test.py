import sys
from PyQt5.QtWidgets import *

from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtWidgets

SERVER = 'MEDISYS-SOFT5\SQLEXPRESS,49677'
DATABASE = 'userdb'
USERNAME = 'teja'
PASSWORD = '7799'


connString = f'DRIVER={{SQL Server}};' \
                 f'SERVER={SERVER};' \
                 f'DATABASE={DATABASE}'

global db
db = QSqlDatabase.addDatabase('QODBC')
db.setDatabaseName(connString)

# if db.open():
    # createTableQuery = QSqlQuery()
    # createTableQuery.exec(
    #     """
    #     CREATE TABLE contacts (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    #         name VARCHAR(40) NOT NULL,
    #         job VARCHAR(50),
    #         email VARCHAR(40) NOT NULL
    #     )
    #     """
    # )

