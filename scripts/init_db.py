import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


from database.connection import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    with open("src/database/schema.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()

    print("DB creada correctamente")

if __name__ == "__main__":
    init_db()