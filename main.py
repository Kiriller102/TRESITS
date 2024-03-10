import sqlite3

BD_name = 'database.db'

def create_database():
    conn = sqlite3.connect(BD_name)
    c = conn.cursor()

    # Create User table
    c.execute('''CREATE TABLE IF NOT EXISTS User (
                    ID INTEGER PRIMARY KEY,
                    username TEXT,
                    password TEXT,
                    histRest TEXT,
                    histAns TEXT,
                    isAdmin INTEGER
                )''')

    # Create Chat table
    c.execute('''CREATE TABLE IF NOT EXISTS Chat (
                    ID INTEGER PRIMARY KEY,
                    userID INTEGER,
                    message TEXT,
                    FOREIGN KEY (userID) REFERENCES User(ID_id)
                )''')

    conn.commit()
    conn.close()


def add_user(username, password, histRest, histAns, isAdmin):
    try:
        conn = sqlite3.connect(BD_name)
        c = conn.cursor()

        c.execute('''INSERT INTO User (username, password, histRest, histAns, isAdmin)
                     VALUES (?, ?, ?, ?, ?)''', (username, password, histRest, histAns, isAdmin))

        conn.commit()
        conn.close()
        print("Пользователь успешно добавлен в базу данных.")
    except sqlite3.Error as e:
        print("Ошибка при добавлении пользователя:", e)

def delete_user(userId):
    try:
        conn = sqlite3.connect(BD_name)
        c = conn.cursor()

        c.execute('''DELETE FROM User WHERE ID = ?''', (userId,))

        conn.commit()
        conn.close()
        print("Пользователь успешно удален из базы данных.")
    except sqlite3.Error as e:
        print("Ошибка при удалении пользователя:", e)

def get_all_users():
    try:
        conn = sqlite3.connect(BD_name)
        c = conn.cursor()

        c.execute('''SELECT * FROM User''')
        users = c.fetchall()

        conn.close()
        return users
    except sqlite3.Error as e:
        print("Ошибка при получении пользователей из базы данных:", e)
        return None

def get_user_by_id(userId):
    try:
        conn = sqlite3.connect('my_database.db')
        c = conn.cursor()

        c.execute('''SELECT * FROM User WHERE ID = ?''', (userId,))
        user_info = c.fetchone()

        conn.close()
        return user_info
    except sqlite3.Error as e:
        print("Ошибка при получении информации о пользователе из базы данных:", e)
        return None

def update_user_by_id(user_id, newUsername, newPassword, newHistRest, newHistAns, newIsAdmin):
    try:
        conn = sqlite3.connect(BD_name)
        c = conn.cursor()

        c.execute('''UPDATE User 
                     SET username = ?, password = ?, histRest = ?, histAns = ?, isAdmin = ? 
                     WHERE ID = ?''',
                  (newUsername, newPassword, newHistRest, newHistAns, newIsAdmin, user_id))

        conn.commit()
        conn.close()
        print("Информация успешно обновлена.")
    except sqlite3.Error as e:
        print("Ошибка при обнолении информации пользователя:", e)

def delete_all_users():
    try:
        conn = sqlite3.connect(BD_name)
        c = conn.cursor()

        c.execute('''DELETE FROM User''')

        conn.commit()
        conn.close()
        print("Все пользователи успешно удалены.")
    except sqlite3.Error as e:
        print("Ошибка при удалении всех пользователей:", e)


def add_message(userID, message):
    try:
        conn = sqlite3.connect(BD_name)
        c = conn.cursor()

        c.execute('''INSERT INTO Chat (userID, message)
                     VALUES (?, ?)''', (userID, message))

        conn.commit()
        conn.close()
        print("Сообщение успешно добавлено в базу данных.")
    except sqlite3.Error as e:
        print("Ошибка при добавлении сообщения:", e)

def get_all_messages():
    try:
        conn = sqlite3.connect(BD_name)
        c = conn.cursor()

        c.execute('''SELECT * FROM Chat ORDER BY ID DESC''')
        messages = c.fetchall()

        conn.close()
        return messages
    except sqlite3.Error as e:
        print("Ошибка при получении сообщений из базы данных:", e)
        return None

def delete_all_messages():
    try:
        conn = sqlite3.connect(BD_name)
        c = conn.cursor()

        c.execute('''DELETE FROM Chat''')

        conn.commit()
        conn.close()
        print("Все сообщения успешно удалены.")
    except sqlite3.Error as e:
        print("Ошибка при удалении всех сообщений:", e)

def delete_message(messageID):
    try:
        conn = sqlite3.connect(BD_name)
        c = conn.cursor()

        c.execute('''DELETE FROM Chat WHERE ID = ?''', (messageID,))

        conn.commit()
        conn.close()
        print("Сообщение успешно удалено из базы данных.")
    except sqlite3.Error as e:
        print("Ошибка при удалении сообщения:", e)

def get_messages_by_user_id(userID):
    try:
        conn = sqlite3.connect(BD_name)
        c = conn.cursor()

        c.execute('''SELECT * FROM Chat WHERE userID = ?''', (userID,))
        messages = c.fetchall()

        conn.close()
        return messages
    except sqlite3.Error as e:
        print("Ошибка при получении сообщений из базы данных:", e)
        return None