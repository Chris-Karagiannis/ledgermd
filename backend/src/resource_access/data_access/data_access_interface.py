from abc import ABC, abstractmethod

class DataAccessInterface(ABC):
    @abstractmethod
    def get_all_accounts(self):
        pass