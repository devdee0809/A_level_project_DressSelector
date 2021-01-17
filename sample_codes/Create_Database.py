"""
Table rows have a 64-bit signed integer ROWID which is unique among all rows in the same table
We will use this as the unique PK for all tables
"""

import sqlite3


class DataBaseClass:
    def __init__(self, database_name):
        super().__init__()

        self.cnxn = sqlite3.connect(database_name)
        print('database connected...')

        self.cursor = self.cnxn.cursor()

    def create_user_table(self):
        self.cursor.execute("""
        CREATE TABLE USER 
          ( 
             surname  VARCHAR(40) NOT NULL, 
             forename VARCHAR(40) NOT NULL, 
             email    VARCHAR(40) NOT NULL, 
             password VARCHAR(40) NOT NULL, 
             type     VARCHAR(10) NOT NULL 
          );  
        """)

        self.cnxn.commit()

    def create_admin_requests_table(self):
        self.cursor.execute("""
        CREATE TABLE ADMIN_REQUESTS
          ( 
             user_id  SMALLINT UNSIGNED NOT NULL REFERENCES USER(rowid),
             granted  VARCHAR(3) NOT NULL
          );
        """)

        self.cnxn.commit()

    def create_access_requests(self):
        self.cursor.execute("""
        CREATE TABLE ACCESS_REQUESTS
          ( 
             user1_id    SMALLINT UNSIGNED NOT NULL REFERENCES user(rowid), 
             user2_id    SMALLINT UNSIGNED NOT NULL REFERENCES user(rowid), 
             access_type VARCHAR(4) NOT NULL, 
             granted     VARCHAR(3) NOT NULL
          );
        """)

        self.cnxn.commit()

    def create_shoot_table(self):
        self.cursor.execute("""
        CREATE TABLE SHOOT 
          ( 
             user_id                 SMALLINT UNSIGNED NOT NULL REFERENCES user(rowid),
             score                   FLOAT(2, 2) NOT NULL,
             event                   VARCHAR(40) NOT NULL,
             date                    DATE NOT NULL,
             distance                SMALLINT UNSIGNED NOT NULL,
             distance_unit           VARCHAR(20),
             target_type             VARCHAR(20),
             shoot_type              VARCHAR(20) NOT NULL,
             coached                 VARCHAR(3) NOT NULL,
             coach_name              VARCHAR(40),
             ammo                    VARCHAR(20),
             weather                 VARCHAR(20),
             range_name              VARCHAR(20),
             wind_condition          VARCHAR(20),
             wind_bracket            VARCHAR(20),
             elevation               VARCHAR(10),
             comments                TEXT,
             photo_path              VARCHAR(200)
          );
        """)

        self.cnxn.commit()

    def insert_admin(self, surname, forename, email, password):
        self.cursor.execute("INSERT INTO USER VALUES (?, ?, ?, ?, 'admin')",
                            (surname, forename, email, password))
        print(f'{self.cursor.rowcount} record(s) were modified...')
        self.cnxn.commit()


def main():
    database = DataBaseClass('database.db')
    database.create_user_table()
    database.create_admin_requests_table()
    database.create_access_requests()
    database.create_shoot_table()
    database.insert_admin('fname', 'lname', 'email', 'password')


if __name__ == '__main__':
    main()
