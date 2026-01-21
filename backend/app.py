from flask import Flask, send_from_directory, jsonify
from src.resource_access.data_access import SQLDataAccess
from src.business_logic.account_manager import AccountManager

dist_path = "../frontend/dist"
app = Flask(__name__, static_folder=dist_path, static_url_path='')

data_access = SQLDataAccess()
account_manager = AccountManager(data_access)


# Serve HTML
@app.route('/', defaults={'path': ''})
@app.route("/<string:path>")
def index(path):
    return send_from_directory(app.static_folder, 'index.html')

@app.get("/api/accounts")
def get_accounts():
    accounts = account_manager.get_accounts_list()
    return jsonify(accounts)

if __name__ == '__main__':
    app.run(debug=True)