import sqlite3
import uuid

class Profile:
    def __init__(self) -> None:
        self.cx = sqlite3.connect("chipa.db", check_same_thread=False)
    def GetProfile(self, UID):
        command = f"SELECT * FROM Profiles WHERE id={UID}"
        data = self.cx.execute(command)
        self.cx.commit()
        return data.fetchone()
    def CreateProfile(self, name, email, password):
        try:
            command = f"INSERT INTO Profiles (name, email, password, uid) VALUES (?, ?, ?, ?)"
            data = self.cx.execute(command, (name, email, password))
            self.cx.commit()
            return {"Sample data": data, "PreProcessed data": data.fetchone(), "Message" : "Success"}
        except Exception as e:
            return {"Error" : f"{e}"}

class _db_helper:
    def __init__(self) -> None:
        self.cx = sqlite3.connect("chipa.db", check_same_thread=False)
    def CreateTable(self, tbl_name: str, tbl_columns: dict = None):
        command = f"CREATE TABLE {tbl_name}(id, name, email, password, uid)"
        self.cx.commit()
        self.cx.execute(command)
    def CreateUID(self):
        return uuid.uuid4()