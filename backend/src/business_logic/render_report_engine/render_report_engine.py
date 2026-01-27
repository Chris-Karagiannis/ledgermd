from flask import render_template_string
from src.resource_access.data_access import DataAccessInterface

class RenderReportEngine:
    def __init__(self, data_access: DataAccessInterface):
        self.macros = '{% from "macros.j2" import currency, account, account_balances, account_details with context %}\n'
        self.data_access = data_access

    def render_report(self, markdown: str):
        account_balances = self.data_access.get_all_account_balances()
        entries = self.data_access.get_all_account_details()
        markdown = self.macros + markdown
        rendered_markdown = render_template_string(markdown, accounts=account_balances, entries=entries)
        return rendered_markdown