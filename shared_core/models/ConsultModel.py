import mysql.connector
from datetime import datetime
from mysql.connector import errors

class ConsultModel():

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
        try:
            today = datetime.today().date()

            self.c.execute("""
            SELECT c.ID, c.C_Date, u.LastName, u.FirstName, c.Title, c.Description, t.Stamp 
            FROM consult AS c
            JOIN users AS u ON c.ID_users = u.ID
            JOIN time_stamps AS t ON c.ID_stamp = t.ID
            WHERE c.ID_teachers = %s 
            AND c.C_Date >= %s
            ORDER BY c.C_Date ASC
        """, (current_teacher, today))

            results = self.c.fetchall()
        except Exception:
            pass

        return results
    
    def delete_by_id(self, consult_id):
        try:
            self.c.execute("DELETE FROM consult WHERE ID = %s", (consult_id,))
            self.db.commit()
            return True
        except Exception:
            return False
    
    def consultsU(self, current_user):
        try:
            today = datetime.today().date()

            self.c.execute("""
            SELECT c.ID, c.C_Date, u.LastName, u.FirstName, c.Title, c.Description, t.Stamp 
            FROM consult AS c
            JOIN users AS u ON c.ID_teachers = u.ID
            JOIN time_stamps AS t ON c.ID_stamp = t.ID
            WHERE c.ID_users = %s 
            AND c.C_Date >= %s
            ORDER BY c.C_Date ASC
        """, (current_user, today))

            results = self.c.fetchall()
        except Exception:
            pass

        return results