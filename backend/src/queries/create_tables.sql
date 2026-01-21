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

INSERT OR IGNORE INTO Accounts (id, name, type) VALUES 
    (200, 'Sales', 4),
    (370, 'Fuel & Oil', 5);

CREATE TABLE IF NOT EXISTS Journals (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    narration TEXT
);

CREATE TABLE IF NOT EXISTS Entries (
    id INTEGER PRIMARY KEY,
    journal_id INTEGER,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY(journal_id) REFERENCES Journals(id)
);