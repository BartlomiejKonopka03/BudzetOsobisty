import hashlib
import json
import os

USERS_FILE = "data/users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def ensure_user_file():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, mode="w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)

def load_users():
    ensure_user_file()
    with open(USERS_FILE, encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def register_user(username, password):
    users = load_users()
    if any(u["username"] == username for u in users):
        return None

    hash_pw = hash_password(password)
    users.append({"username": username, "password_hash": hash_pw})
    save_users(users)
    return username

def login_user(username, password):
    users = load_users()
    hash_pw = hash_password(password)
    for u in users:
        if u["username"] == username and u["password_hash"] == hash_pw:
            return username
    return None
