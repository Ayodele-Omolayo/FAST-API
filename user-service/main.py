from fastapi import FastAPI

# FastAPI application instance
app = FastAPI()

# Dummy data
users_db = [
    {"id": 1, "username": "john_doe", "email": "john@example.com", "active": True},
    {"id": 2, "username": "jane_smith", "email": "jane@example.com", "active": True},
    {"id": 3, "username": "bob_wilson", "email": "bob@example.com", "active": False}
]

@app.get("/")
def health():
    return {"message": "User Service Running"}

@app.get("/users")
def get_users():
    return {"users": users_db}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users_db if u["id"] == user_id), None)
    return user if user else {"error": "User not found"}

@app.post("/register")
def register_user(username: str, password: str):
    return {"message": f"User {username} registered successfully", "user_id": len(users_db) + 1}

@app.post("/login")
def login_user(username: str, password: str):
    return {"message": f"User {username} logged in", "token": "dummy_jwt_token_123"}

@app.put("/users/{user_id}/activate")
def activate_user(user_id: int):
    return {"message": f"User {user_id} activated"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted"}
