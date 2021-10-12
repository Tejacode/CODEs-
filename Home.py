# from PyQt5.QtSql import QSqlDatabase
#
# SERVER = 'MEDISYS-SOFT5\SQLEXPRESS,49677'
# DATABASE = 'userdb'
# USERNAME = 'teja'
# PASSWORD = '7799'
# global db
# db = QSqlDatabase.addDatabase('QODBC')
# db.setDatabaseName(f'Driver={{SQL SERVER}}; Server={SERVER}; Database={DATABASE}; UID={USERNAME}; PWD={PASSWORD}')
# print(db.open())
# print(db.isOpen())


from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QTableView, QApplication
import sys

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


def displayData(sqlStatement):
    print('processing query...')
    qry = QSqlQuery(db)
    qry.prepare(sqlStatement)
    qry.exec()

    model = QSqlQueryModel()
    model.setQuery(qry)


    view = QTableView()
    view.setModel(model)
    return view


if __name__ == '__main__':
    app = QApplication(sys.argv)

    if createConnection():
        SQL_STATEMENT = 'SELECT * FROM dbo.pdftest'
        dataView = displayData(SQL_STATEMENT)
        dataView.show()

    app.exit()
    sys.exit(app.exec_())