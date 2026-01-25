from abc import ABC, abstractmethod

class DataAccessInterface(ABC):
    @abstractmethod
    def get_all_accounts(self):
        pass

    @abstractmethod
    def create_journal(self, date: str, narration: str, entries: list[dict]) -> int:
        pass

    @abstractmethod
    def get_all_account_balances(self) -> dict:
        pass

    @abstractmethod
    def create_report(self, markdown: str) -> int:
        pass

    @abstractmethod
    def get_report(self, report_id: int) -> str:
        pass