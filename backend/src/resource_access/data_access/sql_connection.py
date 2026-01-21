import sqlite3

class SQLConnection:
    """Singleton to allow for shared SQLite connection."""

    _instance = None
    _connection = None

    def __new__(cls):
        """Ensures only one instance can be created."""

        if cls._instance is None:
            cls._instance = super(SQLConnection, cls).__new__(cls)

        return cls._instance
    
    def __init__(self, path: str = "data.db"):
        """Creates SQLite connection if it has not been established yet."""

        if self._connection is None:
            self._connection = sqlite3.connect(path, check_same_thread=False)
            self._connection.row_factory = sqlite3.Row
            self.create_tables()

    def create_tables(self):
        cursor = self._connection.cursor()
        sql_file = open('./src/queries/create_tables.sql', 'r')
        sql_script = sql_file.read()
        cursor.executescript(sql_script)
        
    def get_connection(self):
        """Return the SQLite connection."""

        return self._connection