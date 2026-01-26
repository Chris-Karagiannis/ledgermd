from src.resource_access.data_access import DataAccessInterface
from src.business_logic.render_report_engine import RenderReportEngine

class ReportManager:
    def __init__(self, data_access: DataAccessInterface):
        self.data_access = data_access
        self.render_report_engine = RenderReportEngine()

    def preview_report(self, markdown: str):
        account_balances = self.data_access.get_all_account_balances()
        rendered_markdown = self.render_report_engine.render_report(markdown, account_balances)
        return rendered_markdown

    def save_report(self, title: str, markdown: str):
        if not title:
            raise Exception("Report title not entered.")

        report_id = self.data_access.create_report(title, markdown)
        return report_id
    
    def view_report(self, report_id: int):
        markdown = self.data_access.get_report(report_id)
        if markdown:
            account_balances = self.data_access.get_all_account_balances()
            rendered_markdown = self.render_report_engine.render_report(markdown, account_balances)
            return rendered_markdown
        else:
            return None
        
    def list_reports(self):
        reports = self.data_access.get_all_reports()
        return reports