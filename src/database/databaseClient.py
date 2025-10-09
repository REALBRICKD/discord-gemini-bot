import sqlite3

class DatabaseClient:
    def __init__(self, db_path='messagehistory.db'):
        self.db_path = db_path
        self._ensure_tables()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _ensure_tables(self):
        with self._get_connection() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS messages(user_id INT, message_content STRING, bot_response STRING)"
            )

    def save_message(self, user_id, message_content, bot_response):
        with self._get_connection() as conn:
            conn.execute(
                "INSERT INTO messages(user_id, message_content, bot_response) VALUES (?, ?, ?)",
                (user_id, message_content, bot_response)
            )
            conn.commit()

    # get key data
    def get_msg_history(self, user_id):
        with self._get_connection() as conn:
            conn.execute("SELECT message_content, bot_response FROM messages WHERE user_id = ?", (user_id,))
            conn.commit()
        rows = conn.fetchall()
        # Returns a list of (user_message, bot_response) tuples
        return rows

    def delete_user_messages(self, user_id):
        with self._get_connection() as conn:
            conn.execute("DELETE FROM messages WHERE user_id = ?", (user_id,))
            conn.commit()