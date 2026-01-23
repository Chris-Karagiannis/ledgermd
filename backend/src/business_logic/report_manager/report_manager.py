from src.resource_access.data_access import DataAccessInterface
from flask import render_template_string

class ReportManager:
    def __init__(self, data_access: DataAccessInterface):
        self.data_access = data_access

    def render_report(self, markdown: str):
        account_balances = self.data_access.get_all_account_balances()
        rendered_markdown = render_template_string(markdown, accounts=account_balances)
        return rendered_markdown