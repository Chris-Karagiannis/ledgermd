from src.resource_access.data_access import DataAccessInterface
from src.business_logic.models import Account

class AccountManager:
    def __init__(self, data_access: DataAccessInterface):
        self.data_access = data_access
    
    def get_accounts_list(self) -> list[Account]:
        accounts = self.data_access.get_all_accounts()
        return accounts