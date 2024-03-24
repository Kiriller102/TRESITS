from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from DB import DBManager

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    password: str
    isAdmin: int

class Message(BaseModel):
    userId: int
    message: str

class history(BaseModel):
    userId: int
    histRest: str
    histAns: str

DB_name = 'test_database.db'

DB  = DBManager(DB_name)

# Роуты

# Users
@app.post("/users/")
async def create_user(user: User):
    DB.add_user(user.username, user.email, user.password, user.isAdmin)
    return {"user": user}

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    DB.update_user(user_id, user.username, user.email, user.password, user.isAdmin)
    return {"user": user}

@app.get("/users/")
async def read_users():
    return DB.get_all_users()

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user = DB.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    DB.delete_user(user_id)
    return {"message": "User deleted successfully"}


# Messages
@app.post("/messages/")
async def create_message(message: Message):
    DB.add_message(message.userId, message.message)
    return {"message": message}

@app.get("/messages/{user_id}")
async def read_messages(user_id: int):
    messages = DB.get_messages_by_user_id(user_id)
    if messages is None:
        raise HTTPException(status_code=404, detail="Messages not found")
    return messages

@app.get("/messages/")
async def read_all_messages():
    return DB.get_all_messages()

@app.delete("/messages/{message_id}")
async def delete_message(message_id: int):
    DB.delete_message(message_id)
    return {"message": "Message deleted successfully"}

# History
@app.post("/history/")
async def create_history(history: history):
    DB.add_history(history.userId, history.histRest, history.histAns)
    return {"history": history}

@app.get("/history/{user_id}")
async def read_history(user_id: int):
    history = DB.get_history_by_user_id(user_id)
    if history is None:
        raise HTTPException(status_code=404, detail="History not found")
    return history

@app.delete("/history/{history_id}")
async def delete_history(history_id: int):
    DB.delete_history(history_id)
    return {"history": "History deleted successfully"}

# Black list

@app.post("/blacklist/")
async def create_blacklist(user_id: int):
    DB.add_blacklist(user_id)
    return {"message": "User added to blacklist"}

@app.get("/blacklist/{user_email}")
async def read_blacklist(user_email: str):
    user = DB.get_user_by_email(user_email)
    return user

@app.delete("/blacklist/{userEmail}")
async def delete_blacklist(userEmail: int):
    DB.delete_blacklist(userEmail)
    return {"message": "User deleted from blacklist"}