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

    def create_item_catalogue_table(self):
        self.cursor.execute(
            """
        CREATE TABLE "ITEMCATALOGUE" (
            "ItemID" INTEGER NOT NULL,
            "Subcategory"	TEXT NOT NULL,
            "Gender"	TEXT NOT NULL,
            "Season"	TEXT NOT NULL,
            "Colour"	TEXT NOT NULL,
            "Image"	BLOB NOT NULL
        );
        """
        )

        self.cnxn.commit()

    def create_saved_outfits(self):
        self.cursor.execute(
            """
        CREATE TABLE "SAVEDOUTFITS" (
            "Headwear"	INTEGER REFERENCES "ITEMCATALOGUE"("ItemID"),
            "Topwear"	INTEGER REFERENCES "ITEMCATALOGUE"("ItemID"),
            "Bottomwear"	INTEGER REFERENCES "ITEMCATALOGUE"("ItemID"),
            "Shoes"	INTEGER REFERENCES "ITEMCATALOGUE"("ItemID")
        );
        """
        )

        self.cnxn.commit()

    def create_table_preferences(self):
        self.cursor.execute(
            """
        CREATE TABLE "PREFERENCES" (
            "UserID"	INTEGER NOT NULL REFERENCES "USERS"("rowid"),
            "ItemID"	INTEGER NOT NULL REFERENCES "ITEMCATALOGUE"("ItemID"),
            "Rating"	INTEGER NOT NULL
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
    database.create_saved_outfits()
    database.create_table_preferences()


if __name__ == "__main__":
    main()
