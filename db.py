import psycopg2
from config import DB_PASSWORD

class DataBase:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="bot-db",
            user="postgres",
            password=DB_PASSWORD
        )
        self.connection.set_session(autocommit=True)

    # def test(self):
    #     with self.connection.cursor() as cursor:
    #         cursor.execute("""
    #         SELECT * FROM users
    #         """)
    #         result = cursor.fetchone()
    #     print(result)

