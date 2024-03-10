## SQLite Database Management System 

### Requirements

- Python 3.x
- SQLite3

### Usage

1. **Database Creation**
   
   ```python
   create_database()
   ```

   This function creates a SQLite database file named `database.db` and initializes two tables: `User` and `Chat`.

2. **Adding a User**
   
   ```python
   add_user(username, password, histRest, histAns, isAdmin)
   ```

   Adds a new user to the `User` table with the specified parameters.

3. **Deleting a User**
   
   ```python
   delete_user(userId)
   ```

   Deletes a user from the `User` table based on the given user ID.

4. **Getting All Users**
   
   ```python
   get_all_users()
   ```

   Retrieves all users from the `User` table.

5. **Getting User by ID**
   
   ```python
   get_user_by_id(userId)
   ```

   Retrieves user information from the `User` table based on the provided user ID.

6. **Updating User Information**
   
   ```python
   update_user_by_id(user_id, newUsername, newPassword, newHistRest, newHistAns, newIsAdmin)
   ```

   Updates the information of a user in the `User` table with the specified user ID.

7. **Deleting All Users**
   
   ```python
   delete_all_users()
   ```

   Deletes all users from the `User` table.

8. **Adding a Message**
   
   ```python
   add_message(userID, message)
   ```

   Adds a message to the `Chat` table associated with the given user ID.

9. **Getting All Messages**
   
   ```python
   get_all_messages()
   ```

   Retrieves all messages from the `Chat` table.

10. **Deleting All Messages**
    
    ```python
    delete_all_messages()
    ```

    Deletes all messages from the `Chat` table.

11. **Deleting a Message**
    
    ```python
    delete_message(messageID)
    ```

    Deletes a message from the `Chat` table based on the given message ID.

12. **Getting Messages by User ID**
    
    ```python
    get_messages_by_user_id(userID)
    ```

    Retrieves all messages associated with the provided user ID from the `Chat` table.

### Example

```python
from DB import *

# Example usage:
add_user('JohnDoe', 'password123', 'history1', 'history2', 0)
```

This script provides a flexible interface to interact with the SQLite database, enabling easy management of users and messages.
