from dataclasses import dataclass

@dataclass
class Entry:
    id: int
    journal_id: int
    account_id: int
    description: str
    ammount: int