import mysql.connector
from mysql.connector import errors

class TimeStampsModel():

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

    def delStamps(self, current_day, user):
        current_day += 1
        self.c.execute(
            "DELETE FROM teachers_days_time WHERE ID_teachers = %s AND ID_days = %s",
            (user, current_day,)
        )
        self.db.commit()

    def _saveTime(self, select, current_day, user):
        current_day += 1
        select += 1
        try:
            self.c.execute(
                "INSERT INTO teachers_days_time (ID_teachers, ID_days, ID_time) VALUES (%s, %s, %s)",
                (user, current_day, select,)
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

    def daysID(self, current_teacher):
        unique_ids = []
        try:
            self.c.execute("SELECT DISTINCT ID_days FROM teachers_days_time WHERE ID_teachers = %s",
                           (current_teacher,)
            )
            results = self.c.fetchall()
            unique_ids = [row[0] for row in results]
        except:
            pass
        return unique_ids

    def _stampsID(self, current_teacher, day):
        day += 1
        unique_ids = []
        try:
            self.c.execute("SELECT ID_time FROM teachers_days_time WHERE ID_teachers = %s && ID_days = %s",
                           (current_teacher, day,)
                           )
            results = self.c.fetchall()
            unique_ids = [row[0] for row in results]
        except:
            pass
        return unique_ids

    def _stamps(self, i):
        response = 0
        try:
            self.c.execute("SELECT Stamp FROM time_stamps WHERE ID = %s", (i,))
            result = self.c.fetchone()
            response = result[0]
        except:
            pass
        return response