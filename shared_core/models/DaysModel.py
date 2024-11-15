import mysql.connector
from mysql.connector import errors

class DaysModel():

    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                database="econsultationdb",
                host="localhost",
                user="root",
                password="",
                charset="utf8"
            )
        except errors.InterfaceError as e:
            print('\033[31mBaza danych nie odpowiada! Sprawdź połączenie z bazą MySQL!\033[0m')
            exit(1)
        self.c = self.db.cursor()

    def days(self, i):
        response = 0
        result = None
        try:
            self.c.execute("SELECT Day FROM days WHERE ID = %s", (i,))
            result = self.c.fetchone()
            if result:
                response = result[0]
            else:
                response = 0
        except:
            pass

        return response