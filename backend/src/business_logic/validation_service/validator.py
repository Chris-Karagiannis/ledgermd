from abc import ABC, abstractmethod

class Validator(ABC):
    """Abstract base class for Validators."""

    @abstractmethod
    def validate(self, data) -> str|None:
        """Tests data against specified rule, returning string containing error if data is invalid."""
        pass