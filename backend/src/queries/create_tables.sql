CREATE TABLE IF NOT EXISTS AccountType (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT OR IGNORE INTO AccountType (id, name) VALUES 
    (1, 'Asset'), 
    (2, 'Liability'), 
    (3, 'Equity'), 
    (4, 'Income'), 
    (5, 'Expense');

CREATE TABLE IF NOT EXISTS Accounts (
    id INTEGER PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    type INTEGER NOT NULL,
    FOREIGN KEY(type) REFERENCES AccountType(id)
);

-- ASSETS
INSERT OR IGNORE INTO Accounts (id, name, type) VALUES
    (100, 'Cash', 1),
    (110, 'Accounts Receivable', 1),
    (120, 'Inventory', 1),
    (130, 'Prepaid Expenses', 1),
    (140, 'Property, Plant & Equipment', 1),
    (150, 'Accumulated Depreciation', 1);

-- LIABILITIES
INSERT OR IGNORE INTO Accounts (id, name, type) VALUES
    (200, 'Accounts Payable', 2),
    (210, 'Accrued Expenses', 2),
    (220, 'Notes Payable', 2),
    (230, 'Taxes Payable', 2),
    (240, 'Unearned Revenue', 2);

-- EQUITY
INSERT OR IGNORE INTO Accounts (id, name, type) VALUES
    (310, 'Retained Earnings', 3);


-- INCOME
INSERT OR IGNORE INTO Accounts (id, name, type) VALUES
    (400, 'Service Revenue', 4),
    (410, 'Interest Income', 4),
    (420, 'Sales', 4), -- already had 200 as Sales, could skip
    (430, 'Rental Income', 4);

-- EXPENSES
INSERT OR IGNORE INTO Accounts (id, name, type) VALUES
    (500, 'Salaries & Wages', 5),
    (510, 'Rent Expense', 5),
    (520, 'Utilities Expense', 5),
    (530, 'Supplies Expense', 5),
    (540, 'Insurance Expense', 5),
    (550, 'Depreciation Expense', 5),
    (560, 'Fuel & Oil', 5), -- already exists
    (570, 'Advertising Expense', 5),
    (580, 'Travel Expense', 5),
    (590, 'Bank Fees', 5);

CREATE TABLE IF NOT EXISTS Journals (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    narration TEXT
);

CREATE TABLE IF NOT EXISTS Entries (
    id INTEGER PRIMARY KEY,
    journal_id INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY(journal_id) REFERENCES Journals(id),
    FOREIGN KEY(account_id) REFERENCES Accounts(id)
);

CREATE TABLE IF NOT EXISTS Reports (
    id INTEGER PRIMARY KEY,
    markdown TEXT NOT NULL
);