import sqlite3

class Profile:
    def __init__(self) -> None:
        self.cx = sqlite3.connect("chipa.db")
    def GetProfile(self, id):
        command = f"SELECT * FROM Profiles WHERE id={id}"
        data = self.cx.execute(command)
        self.cx.commit()
        return data.fetchone()

class _db_helper:
    def __init__(self) -> None:
        self.cx = sqlite3.connect("chipa.db")
    def CreateTable(self, tbl_name: str, tbl_columns: dict = None):
        command = f"CREATE TABLE {tbl_name}(id, name, email, password)"
        self.cx.commit()
        self.cx.execute(command)