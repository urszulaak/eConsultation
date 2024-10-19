import mysql.connector

class UsersModel():

    def __init__(self):
        self.db = mysql.connector.connect(
            database="econsultationdb",
            host="localhost",
            user="root",
            password="",
            charset="utf8"
        )
        if self.db.is_connected():
            print('Connceted')
        else:
            print('not connected')
        self.c = self.db.cursor()


    def add(self, fields):
        response = 0
        try:
            self.c.execute(
                "INSERT INTO users (LastName, FirstName, Login, Password, PhoneNumber, Email) VALUES (%s, %s, %s, %s, %s, %s)",
                (fields[0], fields[1], fields[2], fields[3], fields[4], fields[5])
            )
            self.db.commit()
            response = self.c.rowcount
        except:
            pass


        return response
