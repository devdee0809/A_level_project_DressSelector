import os
import sys
import sqlite3
from datetime import datetime


class DataBaseClass:
    def __init__(self, database_name):
        super().__init__()

        self.cnxn = sqlite3.connect(database_name)
        print('database connected...')

        self.cursor = self.cnxn.cursor()

    def check_user_exists_using_email(self, email):
        row = self.cursor.execute("SELECT * FROM USER WHERE email=?",
                                  [email]).fetchone()
        if row:
            return True
        else:
            return False

    def check_user_exists_using_rowid(self, rowid):
        row = self.cursor.execute("SELECT * FROM USER WHERE rowid=?",
                                  [rowid]).fetchone()
        if row:
            return True
        else:
            return False

    def check_user_password_is_correct(self, email, password):
        row = self.cursor.execute("SELECT * FROM USER WHERE email=?",
                                  [email]).fetchone()
        if row[3] == password:
            return True
        else:
            return False

    def check_admin_request_exists(self, rowid):
        row = self.cursor.execute("""
        SELECT ADMIN_REQUESTS.* 
        FROM   ADMIN_REQUESTS
               INNER JOIN USER
                       ON ADMIN_REQUESTS.user_id = USER.rowid
        WHERE  USER.rowid = ?; 
                                           """, [rowid]).fetchone()

        if row:
            return True
        else:
            return False

    def update_user_surname(self, rowid, surname):
        self.cursor.execute("UPDATE USER SET surname=? WHERE rowid=?",
                            (surname, rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def update_user_forename(self, rowid, forename):
        self.cursor.execute("UPDATE USER SET forename=? WHERE rowid=?",
                            (forename, rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def update_user_email(self, rowid, new_email):
        self.cursor.execute("UPDATE USER SET email=? WHERE rowid=?",
                            (new_email, rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def update_user_password(self, rowid, new_password):
        self.cursor.execute("UPDATE USER SET password=? WHERE rowid=?",
                            (new_password, rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def update_user_type_to_admin(self, rowid):
        self.cursor.execute("UPDATE USER SET type=? WHERE rowid=?",
                            ('admin', rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def update_access_request_type(self, rowid, access_type):
        self.cursor.execute(
            "UPDATE ACCESS_REQUESTS SET access_type=?, granted=? WHERE rowid=?",
            (access_type, 'new', rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def update_user_shoot(
            self, shoot_id, score, event, date, distance, distance_unit,
            target_type, shoot_type, coached, coach_name, ammo, weather,
            range_name, wind_condition, wind_bracket, elevation, comments,
            photo_path):
        self.cursor.execute(
            """
        UPDATE SHOOT 
        SET    score = ?, event = ?, date = ?, distance = ?, distance_unit = ?, target_type = ?, 
               shoot_type = ?, coached = ?, coach_name = ?, ammo = ?, weather = ?, range_name = ?, 
               wind_condition = ?, wind_bracket = ?, elevation = ?, comments = ?, photo_path = ? 
        WHERE  rowid = ?
                            """,
            (score, event, date, distance, distance_unit,
             target_type, shoot_type, coached, coach_name,
             ammo, weather, range_name, wind_condition,
             wind_bracket, elevation, comments, photo_path,
             shoot_id))

        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def insert_new_user(self, surname, forename, email, password):
        self.cursor.execute("INSERT INTO USER VALUES (?, ?, ?, ?, 'local')",
                            (surname, forename, email, password))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def insert_new_shoot(
            self, user_id, score, event, date, distance, distance_unit,
            target_type, shoot_type, coached, coach_name, ammo, weather,
            range_name, wind_condition, wind_bracket, elevation, comments,
            photo_path):

        self.cursor.execute(
            "INSERT INTO SHOOT VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (user_id, score, event, date, distance, distance_unit, target_type,
             shoot_type, coached, coach_name, ammo, weather, range_name,
             wind_condition, wind_bracket, elevation, comments, photo_path))

        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def insert_admin_request(self, rowid):
        self.cursor.execute("INSERT INTO ADMIN_REQUESTS VALUES (?, ?)",
                            (rowid, 'new'))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def insert_access_request(self, user1_id, user2_id, access_type):
        row = self.get_user_access_request(user1_id, user2_id)

        if row:
            self.update_access_request_type(row[0], access_type)
        else:
            row = self.cursor.execute(
                "SELECT rowid, * FROM USER WHERE rowid=?",
                [user1_id]).fetchone()
            self.cursor.execute(
                "INSERT INTO ACCESS_REQUESTS VALUES (?, ?, ?, ?)",
                (row[0],
                 user2_id, access_type, 'new'))

        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def get_other_users_info(self, rowid):
        return self.cursor.execute("SELECT rowid, * FROM USER WHERE rowid!=?",
                                   [rowid]).fetchall()

    def get_user_info(self, rowid):
        return self.cursor.execute("SELECT rowid, * FROM USER WHERE rowid=?",
                                   [rowid]).fetchone()

    def get_user_info_using_email(self, email):
        return self.cursor.execute("SELECT rowid, * FROM USER WHERE email=?",
                                   [email]).fetchone()

    def get_users_admin_requests(self):
        return self.cursor.execute("""
        SELECT user_id,
               surname, 
               forename, 
               granted 
        FROM   USER 
               INNER  JOIN ADMIN_REQUESTS
                        ON USER.rowid = ADMIN_REQUESTS.user_id; 
        """).fetchall()

    def get_users_access_requests(self):
        return self.cursor.execute("""
        SELECT ACCESS_REQUESTS.rowid,
               USER1.surname, 
               USER1.forename,
               USER2.surname, 
               USER2.forename,
               ACCESS_REQUESTS.access_type, 
               ACCESS_REQUESTS.granted 
        FROM   ACCESS_REQUESTS
               INNER  JOIN USER AS USER1
                        ON USER1.rowid = ACCESS_REQUESTS.user1_id
               INNER  JOIN USER AS USER2
                        ON USER2.rowid = ACCESS_REQUESTS.user2_id;  
            """).fetchall()

    def get_user_access_request(self, user1_id, user2_id):
        return self.cursor.execute("""
        SELECT ACCESS_REQUESTS.rowid,
               ACCESS_REQUESTS.* 
        FROM   ACCESS_REQUESTS
               INNER JOIN USER
                       ON ACCESS_REQUESTS.user1_id = USER.rowid
        WHERE  USER.rowid = ? 
               AND ACCESS_REQUESTS.user2_id = ?; 
                                   """, (user1_id, user2_id)).fetchone()

    def get_user_granted_access_requests(self, user1_id):

        row = self.cursor.execute("SELECT * FROM USER WHERE rowid=?",
                                  [user1_id]).fetchone()

        if row[4] == 'admin':
            return self.cursor.execute(
                "SELECT rowid, surname, forename FROM USER WHERE rowid!=?",
                [user1_id]).fetchall()
        else:
            return self.cursor.execute("""
            SELECT USER2.rowid,               
                   USER2.surname, 
                   USER2.forename                
            FROM   ACCESS_REQUESTS
                   INNER  JOIN USER AS USER1
                            ON USER1.rowid = ACCESS_REQUESTS.user1_id
                   INNER  JOIN USER AS USER2
                            ON USER2.rowid = ACCESS_REQUESTS.user2_id
            WHERE USER1.rowid = ? AND ACCESS_REQUESTS.granted = ?; 
                                        """, [user1_id, 'yes']).fetchall()

    def get_user_shoots(self, rowid):
        return self.cursor.execute("""
        SELECT SHOOT.rowid,
               SHOOT.* 
        FROM   SHOOT
               INNER JOIN USER
                       ON SHOOT.user_id = USER.rowid
        WHERE  USER.rowid = ?; 
                                   """, [rowid]).fetchall()

    def get_user_shoot(self, user_rowid, shoot_rowid):
        return self.cursor.execute("""
        SELECT SHOOT.* 
        FROM   SHOOT
               INNER JOIN USER
                       ON SHOOT.user_id = USER.rowid
        WHERE  USER.rowid = ? 
               AND SHOOT.rowid = ?; 
                                   """, (user_rowid, shoot_rowid)).fetchone()

    def delete_user_shoot(self, user_rowid, shoot_rowid):
        self.cursor.execute("""
        DELETE FROM SHOOT 
        WHERE  user_id IN (SELECT rowid 
                           FROM   USER 
                           WHERE  rowid = ?) 
               AND rowid = ?;  
                            """, (user_rowid, shoot_rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def grant_admin_request(self, user_id):
        self.update_user_type_to_admin(user_id)
        self.cursor.execute(
            "UPDATE ADMIN_REQUESTS SET granted=? WHERE user_id=?",
            ('yes', user_id))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def deny_admin_request(self, user_id):
        self.cursor.execute(
            "UPDATE ADMIN_REQUESTS SET granted=? WHERE user_id=?",
            ('no', user_id))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def grant_access_request(self, rowid):
        self.cursor.execute(
            "UPDATE ACCESS_REQUESTS SET granted=? WHERE rowid=?",
            ('yes', rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()

    def deny_access_request(self, rowid):
        self.cursor.execute(
            "UPDATE ACCESS_REQUESTS SET granted=? WHERE rowid=?",
            ('no', rowid))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()


database = DataBaseClass('database.db')
