from .validator import Validator

class Length(Validator):
    """Validator to ensure data stays within specified length."""

    def __init__(self, min_length: int = None, max_length: int = None):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, data) -> str|None:
        if self.min_length and self.max_length:
            if len(data) < self.min_length or len(data) > self.max_length:
                return f"Length must be between {self.min_length} and {self.max_length}"
        elif self.min_length and not self.max_length:
            if len(data) < self.min_length:
                return f"Length must be greater than {self.min_length}"
        elif not self.min_length and self.max_length:
            if len(data) > self.max_length:
                return f"Length must be less than {self.max_length}"