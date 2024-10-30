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


    def _add(self, fields):
        try:
            self.c.execute(
                "INSERT INTO users (LastName, FirstName, Login, Password) VALUES (%s, %s, %s, %s)",
                (fields[1], fields[2], fields[3], fields[4])
            )
            self.db.commit()
            if(fields[0] == 't'):
                self.c.execute(
                "INSERT INTO teachers (ID) SELECT MAX(ID) FROM users"
                )
            self.db.commit()
        except:
            pass

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

    def _days(self, i):
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
