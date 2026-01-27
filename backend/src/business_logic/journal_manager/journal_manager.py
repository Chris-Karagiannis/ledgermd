from src.business_logic.validation_service import ValidationChain, JournalTotal, ContainsAccount
from src.resource_access.data_access import DataAccessInterface

class JournalManager:
    def __init__(self, data_access: DataAccessInterface):
        self.entry_validation = ValidationChain([JournalTotal(), ContainsAccount()])
        self.data_access = data_access

    def post_journal(self, date: str, narration: str, entries: list[dict]):
        if not date:
            raise Exception("No transaction date entered.")
        
        self.entry_validation.validate(entries)
        
        journal_id = self.data_access.create_journal(date, narration, entries)
        
        return journal_id

