import pytest
from flask import Flask
from src.business_logic.report_manager import ReportManager

#TODO: ReportManager: preview_report(), save_report(), update_report(), view_report(), list_reports()
def test_preview_report(report_manager: ReportManager, app: Flask):
    markdown = "{{ account(100) }}"

    with app.app_context():
        rendered_markdown = report_manager.preview_report(markdown)
        assert rendered_markdown == "$400.00 DR"
    

def test_save_report(report_manager: ReportManager):
    markdown = "{{ account(100) }}"
    title = "Report Title"
    report_id = report_manager.save_report(title, markdown)
    assert report_id == 1

    with pytest.raises(Exception) as error:
        report_id = report_manager.save_report("", markdown)
    
    assert str(error.value) == "Report title not entered."

def test_update_report(report_manager: ReportManager):
    markdown = "{{ account(420) }}"
    title = "New Report Title"
    report_id = report_manager.update_report(1, title, markdown)
    assert report_id == 1

    with pytest.raises(Exception) as error:
        report_id = report_manager.update_report(1, "", markdown)
    
    assert str(error.value) == "Report title not entered."

    with pytest.raises(Exception) as error:
        report_id = report_manager.update_report(5, title, markdown)

    assert str(error.value) == "Could not update report."

def test_view_report(report_manager: ReportManager, app: Flask):
    with app.app_context():
        report = report_manager.view_report(1)
        assert report["title"] == "New Report Title"
        assert report["raw"] == "{{ account(420) }}"

        report = report_manager.view_report(5)
        assert report == None

def test_list_reports(report_manager: ReportManager):
    reports = report_manager.list_reports()
    assert len(reports) == 1
    assert reports[0]["id"] == 1
    assert reports[0]["title"] == "New Report Title"