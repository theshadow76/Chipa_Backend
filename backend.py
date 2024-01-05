import sqlite3
import uuid
from cryptography.fernet import Fernet

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

class _Admin_helper:
    def __init__(self) -> None:
        self.key = Fernet.generate_key()
        self.fernet = Fernet(key=self.key)
    def str_to_binary(self, string):
        # Initialize empty list to store binary values
        binary_list = []
        
        # Iterate through each character in the string
        for char in string:
            # Convert character to binary, pad with leading zeroes and append to list
            binary_list.append(bin(ord(char))[2:].zfill(8))
            
        # Join the binary values in the list and return as a single string
        return ''.join(binary_list)
    def SaveData(self, data):
        message = str(data)
        with open("Admin.data", 'w') as f:
            f.write(self.str_to_binary(string=message))
        return self.str_to_binary(string=message)
