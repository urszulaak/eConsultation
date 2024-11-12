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
            print('Connected')
        else:
            print('not connected')
        self.c = self.db.cursor()


    def add(self, fields):
        result = None
        try:
            self.c.execute(
                "SELECT ID FROM users WHERE Login = %s",
                (fields[3],)
            )
            result = self.c.fetchone()
            print(result)
            if not result:
                self.c.execute(
                    "INSERT INTO users (FirstName, LastName, Login, Password) VALUES (%s, %s, %s, %s)",
                    (fields[1], fields[2], fields[3], fields[4])
                )
                self.db.commit()
                if(fields[0] == 't' or fields[0] == 'T'):
                    self.c.execute(
                    "INSERT INTO teachers (ID) SELECT MAX(ID) FROM users"
                    )
                self.db.commit()
                result = True
            else:
                result = False
        except:
            pass
        return result

    def _logged(self,fields):
        response = 0
        result = None
        try:
            self.c.execute(
                "SELECT ID FROM users WHERE Login = %s AND Password = %s",
                (fields[0], fields[1])
            )
            result = self.c.fetchone()
            if result:
                response = result[0]
            else:
                response = 0
        except:
            pass
        return response
    
    def _isTeacher(self,fields):
        response = 0
        result = None
        try:
            self.c.execute(
                "SELECT teachers.ID FROM teachers INNER JOIN users ON teachers.ID = users.ID WHERE users.Login = %s AND users.Password = %s",
                (fields[0], fields[1])
            )
            result = self.c.fetchone()
            if result:
                response = result[0]
            else:
                response = 0
        except:
            pass

        return response