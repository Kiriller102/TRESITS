## README: SQLite Database Manager

Этот класс Python, `DBManager`, предоставляет функционал для управления базой данных SQLite. Он включает методы для создания таблиц, добавления, удаления, обновления и извлечения данных из базы данных.

### Зависимости
- Библиотека `sqlite3`

### Использование

1. **Инициализация**: Создайте экземпляр `DBManager`, указав имя файла базы данных SQLite.

    ```python
    db_manager = DBManager('my_database.db')
    ```

2. **Создание базы данных**: Используйте метод `create_database()` для создания необходимых таблиц в базе данных.

    ```python
    db_manager.create_database()
    ```

3. **Добавление пользователя**: Добавьте пользователя в таблицу `User` с помощью метода `add_user()`.

    ```python
    db_manager.add_user('username', 'password', isAdmin)
    ```

4. **Удаление пользователя**: Удалите пользователя из таблицы `User` с помощью метода `delete_user()`.

    ```python
    db_manager.delete_user(user_id)
    ```

5. **Обновление пользователя**: Обновите информацию о пользователе в таблице `User` с помощью метода `update_user_by_id()`.

    ```python
    db_manager.update_user_by_id(user_id, newUsername, newPassword, newIsAdmin)
    ```

6. **Получение пользователей**: Получите информацию о пользователе из таблицы `User` с помощью метода `get_user_by_id()` или `get_all_users()`.

    ```python
    user_info = db_manager.get_user_by_id(user_id)
    all_users = db_manager.get_all_users()
    ```

7. **Добавление сообщения**: Добавьте сообщение в таблицу `Chat` с помощью метода `add_message()`.

    ```python
    db_manager.add_message(user_id, 'message')
    ```

8. **Удаление сообщения**: Удалите сообщение из таблицы `Chat` с помощью метода `delete_message()`.

    ```python
    db_manager.delete_message(message_id)
    ```

9. **Получение сообщений**: Получите сообщения из таблицы `Chat` с помощью метода `get_all_messages()` или `get_messages_by_user_id()`.

    ```python
    all_messages = db_manager.get_all_messages()
    user_messages = db_manager.get_messages_by_user_id(user_id)
    ```

10. **Обработка ошибок**: Класс включает обработку ошибок для операций с базой данных.

    ```python
    try:
        # Операция с базой данных
    except sqlite3.Error as e:
        print("Ошибка:", e)
    ```

### Дополнительные методы

- `delete_all_users()`: Удалить всех пользователей из таблицы `User`.
- `delete_all_messages()`: Удалить все сообщения из таблицы `Chat`.
- `get_user_hist(userID)`: Получить историю пользователя из таблицы `History`.
- `delete_history(histID)`: Удалить историю из таблицы `History`.

### Примечание
:Убедитесь, что файл базы данных SQLite существует и доступен экземпляру класса. Файл базы данных будет создан, если он не существует, при вызове `create_database()`.
