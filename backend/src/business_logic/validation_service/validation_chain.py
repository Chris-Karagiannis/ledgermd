from .validator import Validator
from .exceptions import ValidationError

class ValidationChain:
    """Apply a chain of validators for a specified field using Chain of Responsibility pattern."""

    def __init__(self, validators: list[Validator]):
        self.__validators = validators

    def validate(self, data):
        """Validates data by testing it against each validator, raising error if it fails."""
        
        for validator in self.__validators:
            error = validator.validate(data)

            if error: 
                raise ValidationError(error)
