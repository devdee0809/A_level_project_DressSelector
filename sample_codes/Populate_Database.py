"""
Storing an integer in sqlite results in BLOBs (binary values) instead of INTEGER in sqlite to fix I used:
https://stackoverflow.com/questions/49456158/integer-in-python-pandas-becomes-blob-binary-in-sqlite
"""
import sqlite3
import numpy as np
import pandas as pd

sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))
sqlite3.register_adapter(np.int8, lambda val: int(val))


class DataBaseClass:
    def __init__(self, database_name):
        super().__init__()

        self.cnxn = sqlite3.connect(database_name)
        print('database connected...')

        self.cursor = self.cnxn.cursor()

    def populate_user_table(self, df_users):
        for row_index, row in df_users.iterrows():
            self.cursor.execute("INSERT INTO USER VALUES (?, ?, ?, ?, ?)",
                                (row['surname'],
                                 row['forename'],
                                 row['email'],
                                 row['password'],
                                 row['type']))

        self.cnxn.commit()

        rows = self.cursor.execute("SELECT rowid, * FROM USER").fetchall()
        for row in rows:
            print(row)

    def populate_admin_requests_table(self, df_admin_requests):
        for row_index, row in df_admin_requests.iterrows():
            self.cursor.execute("INSERT INTO ADMIN_REQUESTS VALUES (?, ?)",
                                (row['user_id'],
                                 row['granted']))
            self.cnxn.commit()

        rows = self.cursor.execute(
            "SELECT rowid, * FROM ADMIN_REQUESTS").fetchall()
        for row in rows:
            print(row)

    def populate_access_requests_table(self, df_access_requests):
        for row_index, row in df_access_requests.iterrows():
            self.cursor.execute(
                "INSERT INTO ACCESS_REQUESTS VALUES (?, ?, ?, ?)",
                (row['user1_id'],
                 row['user2_id'],
                 row['access_type'],
                 row['granted']))
            self.cnxn.commit()

        rows = self.cursor.execute(
            "SELECT rowid, * FROM ACCESS_REQUESTS").fetchall()
        for row in rows:
            print(row)

    def populate_shoot_table(self, df_shoot):
        for row_index, row in df_shoot.iterrows():
            self.cursor.execute(
                "INSERT INTO SHOOT VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (row['user_id'],
                 row['score'],
                 row['event'],
                 row['date'],
                 row['distance'],
                 row['distance_unit'],
                 row['target_type'],
                 row['shoot_type'],
                 row['coached'],
                 row['coach_name'],
                 row['ammo'],
                 row['weather'],
                 row['range_name'],
                 row['wind_condition'],
                 row['wind_bracket'],
                 row['elevation'],
                 row['comments'],
                 row['photo_path']))
            self.cnxn.commit()

        rows = self.cursor.execute("SELECT rowid, * FROM SHOOT").fetchall()
        for row in rows:
            print(row)


def main():
    df_users = pd.read_csv('users.csv', encoding='latin1', index_col='rowid')
    df_admin_requests = pd.read_csv(
        'admin_requests.csv', encoding='latin1', index_col='rowid').assign(
        user_id=lambda df: pd.to_numeric(df['user_id']).astype('int8'))
    df_access_requests = pd.read_csv(
        'access_requests.csv', encoding='latin1', index_col='rowid').assign(
        user1_id=lambda df: pd.to_numeric(df['user1_id']).astype('int8'),
        user2_id=lambda df: pd.to_numeric(df['user2_id']).astype('int8'))
    df_shoot = pd.read_csv('shoot.csv', encoding='latin1', index_col='rowid')

    database = DataBaseClass('database.db')
    database.populate_user_table(df_users)
    database.populate_admin_requests_table(df_admin_requests)
    database.populate_access_requests_table(df_access_requests)
    database.populate_shoot_table(df_shoot)


if __name__ == '__main__':
    main()
