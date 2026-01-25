from flask import render_template_string

class RenderReportEngine:
    def __init__(self):
        self.macros = '{% from "macros.j2" import account, account_balances with context %}\n'

    def render_report(self, markdown: str, account_balances: dict):
        markdown = self.macros + markdown
        rendered_markdown = render_template_string(markdown, accounts=account_balances)
        return rendered_markdown