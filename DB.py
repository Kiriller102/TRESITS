import sqlite3
    
class DBManager:
    def __init__(self, database_name):
        self.DB_name = database_name

    def create_database(self):
        conn = sqlite3.connect(self.DB_name)
        c = conn.cursor()

        # Create User table
        c.execute('''CREATE TABLE IF NOT EXISTS User (
                        ID INTEGER PRIMARY KEY,
                        username TEXT,
                        password TEXT,
                        isAdmin INTEGER
                    )''')

        # Create History table
        c.execute('''CREATE TABLE IF NOT EXISTS History (
                        ID INTEGER PRIMARY KEY,
                        userID INTEGER,
                        histRest TEXT,
                        histAns TEXT,
                        FOREIGN KEY (userID) REFERENCES User(ID)
                    )''')

        # Create Chat table
        c.execute('''CREATE TABLE IF NOT EXISTS Chat (
                        ID INTEGER PRIMARY KEY,
                        userID INTEGER,
                        message TEXT,
                        FOREIGN KEY (userID) REFERENCES User(ID)
                    )''')

        conn.commit()
        conn.close()

    def add_user(self, username, password, isAdmin):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''INSERT INTO User (username, password, isAdmin)
                         VALUES (?, ?, ?)''', (username, password, isAdmin))

            conn.commit()
            conn.close()
            print("Пользователь успешно добавлен в базу данных.")
        except sqlite3.Error as e:
            print("Ошибка при добавлении пользователя:", e)

    def delete_user(self, userId):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''DELETE FROM User WHERE ID = ?''', (userId,))

            conn.commit()
            conn.close()
            print("Пользователь успешно удален из базы данных.")
        except sqlite3.Error as e:
            print("Ошибка при удалении пользователя:", e)

    def get_user_by_id(self, userId):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''SELECT * FROM User WHERE ID = ?''', (userId,))
            user_info = c.fetchone()

            conn.close()
            return user_info
        except sqlite3.Error as e:
            print("Ошибка при получении информации о пользователе из базы данных:", e)
            return None

    def get_all_users(self):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''SELECT * FROM User''')
            users = c.fetchall()

            conn.close()
            return users
        except sqlite3.Error as e:
            print("Ошибка при получении пользователей из базы данных:", e)
            return None

    def update_user_by_id(self, user_id, newUsername, newPassword, newIsAdmin):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''UPDATE User 
                         SET username = ?, password = ?, isAdmin = ? 
                         WHERE ID = ?''',
                      (newUsername, newPassword, newIsAdmin, user_id))

            conn.commit()
            conn.close()
            print("Информация успешно обновлена.")
        except sqlite3.Error as e:
            print("Ошибка при обнолении информации пользователя:", e)

    def delete_all_users(self):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''DELETE FROM User''')

            conn.commit()
            conn.close()
            print("Все пользователи успешно удалены.")
        except sqlite3.Error as e:
            print("Ошибка при удалении всех пользователей:", e)


    def add_message(self, userID, message):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''INSERT INTO Chat (userID, message)
                         VALUES (?, ?)''', (userID, message))

            conn.commit()
            conn.close()
            print("Сообщение успешно добавлено в базу данных.")
        except sqlite3.Error as e:
            print("Ошибка при добавлении сообщения:", e)

    def get_all_messages(self):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''SELECT * FROM Chat ORDER BY ID DESC''')
            messages = c.fetchall()

            conn.close()
            return messages
        except sqlite3.Error as e:
            print("Ошибка при получении сообщений из базы данных:", e)
            return None

    def delete_message(self, messageID):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''DELETE FROM Chat WHERE ID = ?''', (messageID,))

            conn.commit()
            conn.close()
            print("Сообщение успешно удалено из базы данных.")
        except sqlite3.Error as e:
            print("Ошибка при удалении сообщения:", e)

    def delete_all_messages(self):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''DELETE FROM Chat''')

            conn.commit()
            conn.close()
            print("Все сообщения успешно удалены.")
        except sqlite3.Error as e:
            print("Ошибка при удалении всех сообщений:", e)

    def get_messages_by_user_id(self, userID):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''SELECT * FROM Chat WHERE userID = ?''', (userID,))
            messages = c.fetchall()

            conn.close()
            return messages
        except sqlite3.Error as e:
            print("Ошибка при получении сообщений из базы данных:", e)
            return None


    def get_user_hist(self, userID):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''SELECT * FROM History WHERE userID = ?''', (userID,))
            user_hist = c.fetchall()

            conn.close()
            return user_hist
        except sqlite3.Error as e:
            print("Ошибка при получении истории запросов пользователя", e)
            return None

    def delete_history(self, histID):
        try:
            conn = sqlite3.connect(self.DB_name)
            c = conn.cursor()

            c.execute('''DELETE FROM History WHERE ID = ?''', (histID,))

            conn.commit()
            c.close()
        except sqlite3.Error as e:
            print("Ошибка при удалении истории", e)



