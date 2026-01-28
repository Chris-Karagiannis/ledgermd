import pytest
from src.business_logic.journal_manager import JournalManager

#TODO: JournalManager: post_journal()
def test_post_journal(journal_manager: JournalManager):
    date = "2026-01-01"
    narration = "Cash Sale"
    entries = [
        {"account_id": 100, "description": "Cash Received", "amount": 200},
        {"account_id": 420, "description": "Sale Amount", "amount": -200}
    ]
    journal_id = journal_manager.post_journal(date, narration, entries)
    assert journal_id == 1

    # No date entered
    with pytest.raises(Exception) as error:
        journal_id = journal_manager.post_journal(None, narration, entries)
    
    assert str(error.value) == "No transaction date entered."

    # Unbalanced journal
    entries[1]["amount"] = 500

    with pytest.raises(Exception) as error:
        journal_id = journal_manager.post_journal(date, narration, entries)
    
    assert str(error.value) == "Journal entry is not balanced."

    # Only 1 line item
    entries.pop()

    with pytest.raises(Exception) as error:
        journal_id = journal_manager.post_journal(date, narration, entries)
    
    assert str(error.value) == "At least 2 line items required."

    entries.append({"account_id": 420, "description": "Sale Amount", "amount": -200})
    
    # Missing account value
    entries[0]["account_id"] = None

    with pytest.raises(Exception) as error:
        journal_id = journal_manager.post_journal(date, narration, entries)
    
    assert str(error.value) == "Entry missing account."

    entries[0]["account_id"] = 100

    # Ensure amount value with None just becomes 0 when checking
    entries.append({"account_id": 100, "description": "Cash Received", "amount": None})
    journal_id = journal_manager.post_journal(date, narration, entries)
    assert journal_id == 2
    