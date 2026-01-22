from abc import ABC, abstractmethod

class DataAccessInterface(ABC):
    @abstractmethod
    def get_all_accounts(self):
        pass

    @abstractmethod
    def create_journal(self, date: str, narration: str, entries: list[dict]):
        pass