# database_logger.py
import sqlite3

def create_database():
    conn = sqlite3.connect("attack_data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS logs (
                        id INTEGER PRIMARY KEY,
                        action TEXT,
                        result TEXT
                    )""")
    conn.commit()
    conn.close()

def log_action(action, result):
    conn = sqlite3.connect("attack_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (action, result) VALUES (?, ?)", (action, result))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Sample usage
    create_database()
    log_action("phishing", "success")
