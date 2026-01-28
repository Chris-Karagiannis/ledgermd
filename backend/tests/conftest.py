import pytest
from flask import Flask
from src.business_logic.account_manager import AccountManager
from src.business_logic.journal_manager import JournalManager
from src.business_logic.report_manager import ReportManager
from src.resource_access.data_access import SQLDataAccess, SQLConnection
import os

@pytest.fixture
def app():
    return Flask(__name__, template_folder=os.path.join("../", "templates"))

@pytest.fixture
def data_access():
    return SQLDataAccess(":memory:")

@pytest.fixture
def account_manager(data_access):
    return AccountManager(data_access)

@pytest.fixture
def journal_manager(data_access):
    return JournalManager(data_access)

@pytest.fixture
def report_manager(data_access):
    return ReportManager(data_access)