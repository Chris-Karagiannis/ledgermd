from flask import Flask, send_from_directory, jsonify, request
from src.resource_access.data_access import SQLDataAccess
from src.business_logic.account_manager import AccountManager
from src.business_logic.journal_manager import JournalManager
from src.business_logic.report_manager import ReportManager

dist_path = "../frontend/dist"
app = Flask(__name__, static_folder=dist_path, static_url_path='')

data_access = SQLDataAccess()
account_manager = AccountManager(data_access)
journal_manager = JournalManager(data_access)
report_manager = ReportManager(data_access)

# Serve HTML
@app.route('/', defaults={'path': ''})
@app.route("/<string:path>")
def index(path):
    return send_from_directory(app.static_folder, 'index.html')

# Get accounts list
@app.get("/api/accounts")
def get_accounts():
    accounts = account_manager.get_accounts_list()
    return jsonify(accounts)

@app.post("/api/post-journal")
def post_journal():
    data =  request.get_json()
    date, narration, entries = data["date"], data["narration"], data["entries"]
    journal_id = journal_manager.post_journal(date, narration, entries)
    return jsonify({"journal_id": journal_id})

@app.post("/api/preview-markdown")
def preview_markdown():
    data =  request.get_json()
    markdown = data["markdown"]
    rendered_markdown = report_manager.preview_report(markdown)
    return jsonify({"markdown": rendered_markdown})

@app.post("/api/save-report")
def save_report():
    data =  request.get_json()
    markdown = data["markdown"]
    report_id = report_manager.save_report(markdown)
    return jsonify({"report_id": report_id})

@app.get("/api/view-report/<id>")
def view_report(id):
    rendered_markdown = report_manager.view_report(id)
    return jsonify({"markdown": rendered_markdown})

@app.errorhandler(Exception)
def unhandled_error(e):
    print(e)
    response = {"message": str(e)}
    return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)