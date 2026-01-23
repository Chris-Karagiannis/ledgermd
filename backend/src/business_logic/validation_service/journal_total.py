from .validator import Validator

class JournalTotal(Validator):
    def __init__(self, total: int = 0):
        self.total = total
    
    def validate(self, data: list):
        if len(data) < 2:
            return "At least 2 line items required."

        total = 0

        for entry in data:
            if not entry["amount"]:
                entry["amount"] = 0
            total += float(entry["amount"])


        if total != self.total:
            return "Journal entry is not balanced."