from .data_access_interface import DataAccessInterface
from .sql_connection import SQLConnection
from src.business_logic.models import Account
from collections import defaultdict

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
    
    def create_journal(self, date: str, narration: str, entries: list[dict]) -> int:
        cursor = self.connection.cursor()

        sql = "INSERT INTO Journals (date, narration) VALUES (?, ?)"
        cursor.execute(sql, (date, narration))
        journal_id = cursor.lastrowid


        for entry in entries:
            sql = "INSERT INTO Entries (journal_id, account_id, description, amount) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (journal_id, entry["account_id"], entry["description"], entry["amount"]))
        
        self.connection.commit()

        return journal_id

    def get_all_account_balances(self) -> dict:
        cursor = self.connection.cursor()
        sql = """
            SELECT SUM(E.amount) AS total, A.id, A.name FROM Entries AS E
            RIGHT JOIN Accounts AS A ON A.id = E.account_id
            GROUP BY A.id, A.name
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        account_balances = {row["id"]: {"name": row["name"], "amount": row["total"]} for row in rows}
        return account_balances
    
    def create_report(self, title: str, markdown: str) -> int:
        cursor = self.connection.cursor()
        sql = "INSERT INTO Reports (title, markdown) VALUES (?, ?)"
        cursor.execute(sql, (title, markdown))
        report_id = cursor.lastrowid
        self.connection.commit()
        return report_id

    def get_report(self, report_id: int) -> str:
        cursor = self.connection.cursor()
        sql = "SELECT * FROM Reports WHERE id = ?"
        cursor.execute(sql, (report_id, ))
        row = cursor.fetchone()
        report = {"title": row["title"], "markdown": row["markdown"]}
        return report
    
    def get_all_reports(self) -> list:
        cursor = self.connection.cursor()
        sql = "SELECT id, title FROM Reports"
        cursor.execute(sql)
        rows = cursor.fetchall()
        reports = [{"id": row["id"], "title": row["title"]} for row in rows]
        return reports

    def get_all_account_details(self) -> dict:
        cursor = self.connection.cursor()
        sql = """
            SELECT * FROM Entries AS E
            JOIN Journals AS J ON J.id = E.journal_id
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        account_details = defaultdict(list)
        for row in rows:
            entry = {
                "date": row["date"], 
                "narration": row["narration"] if row["narration"] else "", 
                "description": row["description"], 
                "amount": row["amount"]
            }
            account_details[row["account_id"]].append(entry)

        return account_details

    def update_report(self, id: int, title: str, markdown: str) -> int:
        cursor = self.connection.cursor()
        sql = """
            UPDATE Reports
            SET title = ?, markdown = ?
            WHERE id = ?
        """
        cursor.execute(sql, (title, markdown, id))

        if cursor.rowcount == 0:
            return None
        
        self.connection.commit()
        return id