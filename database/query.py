import sqlite3
from pathlib import Path


class DataBase:
    def __init__(self, database_name):

        self.cnxn = sqlite3.connect(database_name, check_same_thread=False)
        print("database connected...")

        self.cursor = self.cnxn.cursor()

        self.first_name = None
        self.last_name = None
        self.gender = None
        self.email = None
        self.password = None

    def check_user_exists(self, by, value):
        if by == "email":
            row = self.cursor.execute(
                "SELECT * FROM USERS WHERE Email=?", [value]
            ).fetchone()

        elif by == "rowid":
            row = self.cursor.execute(
                "SELECT * FROM USERS WHERE rowid=?", [value]
            ).fetchone()

        else:
            return False

        if row:
            # get user's details for later
            (
                self.first_name,
                self.last_name,
                self.gender,
                self.email,
                self.password,
            ) = row

            return True
        else:
            return False

    def check_password_is_correct(self, password):
        if password == self.password:
            return True
        else:
            return False

    def update_user_first_name(self, rowid, first_name):
        self.cursor.execute(
            "UPDATE USERS SET FirstName=? WHERE rowid=?", (first_name, rowid)
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def update_user_last_name(self, rowid, last_name):
        self.cursor.execute(
            "UPDATE USERS SET LastName=? WHERE rowid=?", (last_name, rowid)
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def update_user_email(self, rowid, new_email):
        self.cursor.execute(
            "UPDATE USERS SET Email=? WHERE rowid=?", (new_email, rowid)
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def update_user_password(self, rowid, new_password):
        self.cursor.execute(
            "UPDATE USERS SET Password=? WHERE rowid=?", (new_password, rowid)
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def create_new_user(self, first_name, last_name, gender, email, password):
        self.cursor.execute(
            "INSERT INTO USERS VALUES (?, ?, ?, ?, ?)",
            (first_name, last_name, gender, email, password),
        )
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def delete_user(self, user_rowid):
        self.cursor.execute("DELETE FROM USERS WHERE rowid = ?", (user_rowid))
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def insert_outfit(self, user_rowid):
        self.cursor.execute("INSERT INTO OUTFITS VALUES (?)", (user_rowid))
        print(f"{self.cursor.rowcount} record(s) were modified...")
        self.cnxn.commit()

    def select_random_item_id(self, sub_category):
        row = self.cursor.execute(
            "SELECT * FROM ITEMCATALOGUE WHERE subCategory=? ORDER BY RANDOM() LIMIT 1",
            [sub_category],
        ).fetchone()
        return row["ItemID"]


def main():
    database = DataBase(
        Path(
            "database",
            "database.db",
        )
    )

    database.check_user_exists(by="email", value="JakeSmith@gmail.com")


if __name__ == "__main__":
    main()
