import unittest
import os

import DB
from DB import DBManager

class TestDBManager(unittest.TestCase):
    def setUp(self):
        self.db_manager = DB.DBManager('test_database.db')
        self.db_manager.create_database()

    def tearDown(self):
        os.remove('test_database.db')

    def test_add_user(self):
        self.db_manager.add_user('test_user', 'password', 0)
        users = self.db_manager.get_all_users()
        self.assertEqual(len(users), 1)

    def test_delete_user(self):
        self.db_manager.add_user('test_user', 'password', 0)
        users_before = self.db_manager.get_all_users()
        self.db_manager.delete_user(1)
        users_after = self.db_manager.get_all_users()
        self.assertEqual(len(users_before) - len(users_after), 1)

    def test_get_user_by_id(self):
        self.db_manager.add_user('test_user', 'password', 0)
        user = self.db_manager.get_user_by_id(1)
        self.assertIsNotNone(user)

    def test_add_message(self):
        self.db_manager.add_user('test_user', 'password', 0)
        self.db_manager.add_message(1, 'test_message')
        message = self.db_manager.get_messages_by_user_id(1)
        self.assertIsNotNone(message)


if __name__ == '__main__':
    unittest.main()
