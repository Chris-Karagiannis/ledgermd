from src.resource_access.data_access import DataAccessInterface

class AccountManager:
    def __init__(self, data_access: DataAccessInterface):
        self.data_access = data_access
    
    def get_accounts_list(self):
        accounts = self.data_access.get_all_accounts()
        return accounts