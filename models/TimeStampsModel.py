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
        result = None
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
        response = 0
        try:
            self.c.execute(
                "INSERT INTO teachers_days_time (ID_teachers, ID_days, ID_time) VALUES (%s, %s, %s)",
                (user,current_day+1,select+1,)
            )
            self.db.commit()
            response = self.c.rowcount
        except:
            pass