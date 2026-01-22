from .data_access_interface import DataAccessInterface
from .sql_connection import SQLConnection
from src.business_logic.models import Account, Entry

class SQLDataAccess(DataAccessInterface):
    def __init__(self):
        self.connection = SQLConnection().get_connection()
    
    def get_all_accounts(self):
        cursor = self.connection.cursor()

        sql = "SELECT * FROM Accounts"

        cursor.execute(sql)
        rows = cursor.fetchall()
        accounts = [Account(row["id"], row["name"], row["type"]) for row in rows]
        return accounts
    
    def create_journal(self, date: str, narration: str, entries: list[dict]):
        cursor = self.connection.cursor()

        sql = "INSERT INTO Journals (date, narration) VALUES (?, ?)"
        cursor.execute(sql, (date, narration))
        journal_id = cursor.lastrowid


        for entry in entries:
            sql = "INSERT INTO Entries (journal_id, account_id, description, amount) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (journal_id, entry["account_id"], entry["description"], entry["amount"]))
        
        self.connection.commit()

        return journal_id
            