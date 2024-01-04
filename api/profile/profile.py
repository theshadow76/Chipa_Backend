import sqlite3

class Profile:
    def __init__(self) -> None:
        self.cx = sqlite3.connect("test.db")