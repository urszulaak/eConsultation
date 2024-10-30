import mysql.connector

class TimeStampsModel():

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

    def _timeStamps(self, i):
        response = 0
        try:
            self.c.execute("SELECT Stamp FROM time_stamps WHERE ID = %s", (i,))
            result = self.c.fetchone()
            if result:
                response = result[0]
            else:
                response = 0
        except:
            pass
        return response

    def _saveTime(self, select, current_day, user):
        try:
            self.c.execute(
                "INSERT INTO teachers_days_time (ID_teachers, ID_days, ID_time) VALUES (%s, %s, %s)",
                (user,current_day+1,select+1,)
            )
            self.db.commit()
        except:
            pass

    def _countTeachers(self):
        response = 0
        try:
            self.c.execute("SELECT COUNT(DISTINCT ID_teachers) FROM teachers_days_time")
            result = self.c.fetchone()
            response = result[0]

        except:
            pass
        return response

    def _teachersID(self):
        unique_ids = []
        try:
            self.c.execute("SELECT DISTINCT ID_teachers FROM teachers_days_time")
            results = self.c.fetchall()
            unique_ids = [row[0] for row in results]
        except:
            pass
        return unique_ids

    def _teachers(self, i):
        response = 0
        try:
            self.c.execute("SELECT FirstName, LastName FROM users WHERE ID = %s", (i,))
            result = self.c.fetchone()
            response = f"{result[0]} {result[1]}"
        except:
            pass
        return response

    def _daysID(self,current_teacher):
        unique_ids = []
        try:
            self.c.execute("SELECT DISTINCT ID_days FROM teachers_days_time WHERE Id_teachers = %s",
                           (current_teacher,)
            )
            results = self.c.fetchall()
            unique_ids = [row[0] for row in results]
        except:
            pass
        return unique_ids

    def _days(self, i):
        response = 0
        try:
            self.c.execute("SELECT FirstName, LastName FROM users WHERE ID = %s", (i,))
            result = self.c.fetchone()
            response = f"{result[0]} {result[1]}"
        except:
            pass
        return response