import pytest
from src.business_logic.account_manager import AccountManager
from src.business_logic.models import Account

def test_get_accounts_list(account_manager: AccountManager):
    accounts = account_manager.get_accounts_list()
    cash_account = Account(100, "Cash", 1)
    sales_account = Account(420, "Sales", 4)
    assert cash_account in accounts
    assert sales_account in accounts