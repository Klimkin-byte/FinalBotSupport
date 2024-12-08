import sqlite3
from dotenv import dotenv_values
config_1 = dotenv_values("../.env")
#db_path =config_1.get('DATABASE_PATH')
class Database:
    def __init__(self, db_path=None):
        self.db_path = db_path or config_1.get('DATABASE_PATH')
        self.connection = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, user_id INTEGER, email TEXT, password TEXT,two_factor_ak TEXT,two_factor_aa TEXT,two_factor_an TEXT,two_factor_ae TEXT,name TEXT,date TEXT,Account TEXT,Activating TEXT,KYSREST TEXT,KYSDATA TEXT)"
            )

    def add_user(self, user_id, email, password, two_factor_ak, two_factor_aa,
                 two_factor_an, two_factor_ae, name, date,
                 Account, Activating, KYSREST, KYSDATA):
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO users (
                    user_id, email, password, two_factor_ak, 
                    two_factor_aa, two_factor_an, 
                    two_factor_ae, name, date, 
                    Account, Activating, KYSREST, KYSDATA
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (user_id, email, password, two_factor_ak, two_factor_aa,
                 two_factor_an, two_factor_ae, name, date,
                 Account, Activating, KYSREST,KYSDATA)
            )

    def get_user_by_email(self, email):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(
                "SELECT * FROM users WHERE email = ?", (email,)
            )
            return cursor.fetchone()

    def get_user_by_password(self, password):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(
                "SELECT * FROM users WHERE password = ?", (password,)
            )
            row = cursor.fetchone()
            if row is None:
                return None
            return {
                "id": row[0],
                "user_id": row[1],
                "email": row[2],
                "password": row[3],
                "two_factor_ak": row[4],
                "two_factor_aa": row[5],
                "two_factor_an": row[6],
                "two_factor_ae": row[7],
                "name": row[8],
                "date": row[9],
                "Account": row[10],
                "Activating": row[11],
                "KYSREST": row[12]
            }
            return None

    def update_user_field(self, email, field_name, new_value):
        """
        changes value.
        """
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(
                f"UPDATE users SET {field_name} = ? WHERE email = ?",
                (new_value, email)
            )
            return cursor.rowcount

    def check_multiple_conditions(self, conditions):
        """
        check values in conditions.
        """
        query = "SELECT 1 FROM users WHERE " + " AND ".join(f"{col} = ?" for col in conditions.keys())
        values = tuple(conditions.values())

        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(query, values)
            return cursor.fetchone() is not None

    def add_column_to_table(self,db_path, table_name, column_name, column_type):
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type};"
            cursor.execute(query)

    def get_user_by_email_ch(self,email):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(
                "SELECT * FROM users WHERE email = ?", (email,)
            )
            result = cursor.fetchone()
            print(f"check: {result}")
            return result

    def some_new(self,email):
        print(email)