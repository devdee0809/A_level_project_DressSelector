"""
Table rows have a 64-bit signed integer ROWID which is unique among all rows in
the same table. We will use this as the unique PK for all tables
"""

import sqlite3
from pathlib import Path


class DataBase:
    def __init__(self, database_name):

        self.cnxn = sqlite3.connect(database_name)
        print("database connected...")

        self.cursor = self.cnxn.cursor()

    def create_users_table(self):
        self.cursor.execute(
            """
        CREATE TABLE "USERS" (
            "FirstName"	TEXT NOT NULL,
            "LastName"	TEXT NOT NULL,
            "Gender"	TEXT NOT NULL,
            "Email"	TEXT NOT NULL,
            "Password"	TEXT NOT NULL
        );
        """
        )

        self.cnxn.commit()

    def create_outfit_table(self):
        self.cursor.execute(
            """
        CREATE TABLE "OUTFITS" (
            "UserID"
            INTEGER NOT NULL REFERENCES "USERS"("rowid") 
        );
        """
        )

        self.cnxn.commit()

    def create_item_catalogue_table(self):
        self.cursor.execute(
            """
        CREATE TABLE "ITEMCATALOGUE" (
            "Subcategory"	TEXT NOT NULL,
            "Gender"	TEXT NOT NULL,
            "Season"	TEXT NOT NULL,
            "Colour"	TEXT NOT NULL
        );
        """
        )

        self.cnxn.commit()

    def create_outfit_catalogue_table(self):
        self.cursor.execute(
            """
        CREATE TABLE "OUTFITCATALOGUE" (
            "OutfitID"	INTEGER NOT NULL REFERENCES "OUTFITS"("rowid"),
            "ItemID"	INTEGER NOT NULL REFERENCES "ITEMCATALOGUE"("rowid")
        );
        """
        )

        self.cnxn.commit()


def main():
    database = DataBase(
        Path(
            "database",
            "database.db",
        )
    )
    database.create_users_table()
    database.create_item_catalogue_table()
    database.create_outfit_table()
    database.create_outfit_catalogue_table()


if __name__ == "__main__":
    main()
