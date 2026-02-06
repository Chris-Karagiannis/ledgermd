from src.resource_access.data_access import DataAccessInterface
from src.business_logic.render_report_engine import RenderReportEngine

class ReportManager:
    def __init__(self, data_access: DataAccessInterface):
        self.data_access = data_access
        self.render_report_engine = RenderReportEngine(data_access)

    def preview_report(self, markdown: str) -> str:
        rendered_markdown = self.render_report_engine.render_report(markdown)
        return rendered_markdown

    def save_report(self, title: str, markdown: str) -> int:
        if not title or title == "":
            raise Exception("Report title not entered.")
        try:
            rendered_markdown = self.render_report_engine.render_report(markdown)
        except Exception as e:
            raise Exception("Invalid syntax")
        
        report_id = self.data_access.create_report(title, markdown)
        return report_id

    def update_report(self, id: int, title: str, markdown: str) -> int:
        if not title or title == "":
            raise Exception("Report title not entered.")

        report_id = self.data_access.update_report(id, title, markdown)
        return report_id
    
    def view_report(self, report_id: int) -> dict:
        report = self.data_access.get_report(report_id)
        if report:
            title, markdown = report["title"], report["markdown"]
            rendered_markdown = self.render_report_engine.render_report(markdown)
            result = {"title": title, "markdown": rendered_markdown, "raw": markdown}
            return result
        else:
            return None
        
    def list_reports(self):
        reports = self.data_access.get_all_reports()
        return reports