import sqlite3

# This class handles interactions with the SQLite database for storing and retrieving message history.
class DatabaseClient:
    def __init__(self, db_path='messagehistory.db'):
        self.db_path = db_path
        self._ensure_tables()
    
    # Connect with the database
    def _get_connection(self):
        return sqlite3.connect(self.db_path)
    
    # Create tables if they do not exist
    def _ensure_tables(self):
        with self._get_connection() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS messages(user_id INT, message_content STRING, bot_response STRING)"
            )
    
    # Save a message to the database, along with the bot's response and user's ID
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
            cursor = conn.execute("SELECT message_content, bot_response FROM messages WHERE user_id = ?", (user_id,))
            conn.commit()
        rows = cursor.fetchall()
        return rows

    # Allows a user to clear their own message history from the database
    def delete_user_messages(self, user_id):
        with self._get_connection() as conn:
            conn.execute("DELETE FROM messages WHERE user_id = ?", (user_id,))
            conn.commit()