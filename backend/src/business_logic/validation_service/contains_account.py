from .validator import Validator

class ContainsAccount(Validator):    
    def validate(self, data: list):
        for entry in data:
            if not entry["account_id"]:
                return "Entry missing account."