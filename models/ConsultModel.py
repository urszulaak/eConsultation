import mysql.connector
from datetime import datetime

class ConsultModel():

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

    def addConsult(self, current_teacher, selected_date, current_stamp, form, user):
        try:
            self.c.execute(
                "INSERT INTO consult (ID_teachers, ID_users, Title, Description, C_Date, ID_stamp) VALUES (%s, %s, %s, %s, %s, %s)",
                (current_teacher, user, form[0], form[1], selected_date, current_stamp,)
            )
            self.db.commit()
        except:
            pass

    def consults(self, current_teacher):
        unique_ids = []
        try:
            today = datetime.today().date()

            self.c.execute("""
            SELECT c.C_Date, u.LastName, u.FirstName, c.Title, c.Description, t.Stamp 
            FROM consult AS c
            JOIN users AS u ON c.ID_users = u.ID
            JOIN time_stamps AS t ON c.ID_stamp = t.ID
            WHERE c.ID_teachers = %s 
            AND c.C_Date >= %s
            ORDER BY c.C_Date ASC
        """, (current_teacher, today))

            results = self.c.fetchall()

            for row in results:
                consultation = f"Date: {row[0]} Time: {row[5]} Student: {row[1]} {row[2]} Topic: {row[3]} Description: {row[4]}"
                unique_ids.append([consultation])
        except Exception as e:
            print(f"Error: {e}")

        return unique_ids
    
    def consultsU(self, current_user):
        unique_ids = []
        try:
            today = datetime.today().date()

            self.c.execute("""
            SELECT c.C_Date, u.LastName, u.FirstName, c.Title, c.Description, t.Stamp 
            FROM consult AS c
            JOIN users AS u ON c.ID_teachers = u.ID
            JOIN time_stamps AS t ON c.ID_stamp = t.ID
            WHERE c.ID_users = %s 
            AND c.C_Date >= %s
            ORDER BY c.C_Date ASC
        """, (current_user, today))

            results = self.c.fetchall()

            for row in results:
                consultation = f"Date: {row[0]} Time: {row[5]} Teacher: {row[1]} {row[2]} Topic: {row[3]} Description: {row[4]}"
                unique_ids.append([consultation])
        except Exception as e:
            print(f"Error: {e}")

        return unique_ids