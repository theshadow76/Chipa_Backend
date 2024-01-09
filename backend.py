import sqlite3
import uuid
from cryptography.fernet import Fernet
import requests
import jwt
import os

class Profile:
    def __init__(self) -> None:
        self.cx = sqlite3.connect("chipa.db", check_same_thread=False)
        self.PRIVATE_KEY = os.getenv("CHIPA_PRIVATE_KEY_ADD_PROFILE")
    def GetProfile(self, UID):
        command = f"SELECT * FROM Profiles WHERE id={UID}"
        data = self.cx.execute(command)
        self.cx.commit()
        return data.fetchone()
    def CreateProfile(self, name, email, password):
        try:
            uid = self.CreateUID(email=email, password=password)
            command = f"INSERT INTO ProfilesV2 (uid, email, password) VALUES (?, ?, ?)"
            data = self.cx.execute(command, (uid, email, password))
            self.cx.commit()
            return {"Sample data": data, "PreProcessed data": data.fetchone(), "Message" : "Success"}
        except Exception as e:
            return {"Error" : f"{e}"}
    def SQLExecuter(self, command):
        data = self.cx.execute(command)
        self.cx.commit()
        return {"Message" : data.fetchone()}
    def AddBalance(self, uid: str, balance: float):
        command = f"INSERT INTO Balance (uid, balance) VALUES (?, ?)"
        data = self.cx.execute(command, (uid, balance))
        self.cx.commit()
        return {"Sample data": data, "PreProcessed data": data.fetchone(), "Message" : "Success"}
    def CreateUID(self, email, password):
        data = {
            "email": email,
            "password": password
        }
        print(f"private key = {self.PRIVATE_KEY}") # TODO: Remove this
        token = jwt.encode(payload=data, key=str(self.PRIVATE_KEY), algorithm="HS256")
        return token
    def GetBalance(self, uid):
        command = "SELECT * FROM Balance WHERE uid=?"
        data = self.cx.execute(command, (uid,))
        self.cx.commit()
        dt = data.fetchone()
        return {"ID" : dt[0], "UID" : dt[1], "Balance" : dt[2]}
class Trading:
    def __init__(self) -> None:
        self.url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en"
        self.cx = sqlite3.connect("chipa.db", check_same_thread=False)
    def GetCoins(self):
        response = requests.get(self.url)
        data = response.json()
        return data
    def BuyCrypto(self, uid, amount, type):
        tradeid = uuid.uuid4()
        prfl = Profile()
        data3 = prfl.GetBalance(uid=uid)
        balance = data3['Balance']
        command = f"INSERT INTO CryptoTrading (uid, tradeid, amount, type) VALUES (?, ?, ?, ?)"
        command2 = f"UPDATE Balance SET balance = ? WHERE uid = ?"
        data = self.cx.execute(command, (uid, tradeid, amount, type))
        data2 = self.cx.execute(command2, (balance, uid))

        self.cx.commit()

        return {"Message" : "Success"}

class _db_helper:
    def __init__(self) -> None:
        self.cx = sqlite3.connect("chipa.db", check_same_thread=False)
    def CreateTable(self, tbl_name: str, tbl_columns: dict = None):
        command = f"CREATE TABLE {tbl_name}(uid, tradeid, amount, type)"
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
