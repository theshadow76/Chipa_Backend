import sqlite3

class Profile:
    def __init__(self) -> None:
        self.cx = sqlite3.connect("chipa.db", check_same_thread=False)
    def GetProfile(self, id):
        command = f"SELECT * FROM Profiles WHERE id={id}"
        data = self.cx.execute(command)
        self.cx.commit()
        return data.fetchone()
    def CreateProfile(self, name, email, password):
        try:
            command = f"INSERT INTO Profiles (name, email, password) VALUES (?, ?, ?)"
            data = self.cx.execute(command, (name, email, password))
            self.cx.commit()
            return {"Sample data": data, "PreProcessed data": data.fetchone(), "Message" : "Success"}
        except Exception as e:
            return {"Error" : f"{e}"}

class _db_helper:
    def __init__(self) -> None:
        self.cx = sqlite3.connect("chipa.db", check_same_thread=False)
    def CreateTable(self, tbl_name: str, tbl_columns: dict = None):
        command = f"CREATE TABLE {tbl_name}(id, name, email, password)"
        self.cx.commit()
        self.cx.execute(command)