from .data_access_interface import DataAccessInterface
from .sql_connection import SQLConnection
from src.business_logic.models import Account

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
            