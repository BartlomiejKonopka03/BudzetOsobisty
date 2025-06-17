import csv
import hashlib
import os

USERS_FILE = "data/users.csv"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def ensure_user_file():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password_hash"])

def register_user(username, password):
    ensure_user_file()
    hash_pw = hash_password(password)
    with open(USERS_FILE, mode="r", encoding="utf-8") as file:
        users = list(csv.DictReader(file))
        if any(u["username"] == username for u in users):
            return None  # użytkownik już istnieje
    with open(USERS_FILE, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([username, hash_pw])
    return username

def login_user(username, password):
    ensure_user_file()
    hash_pw = hash_password(password)
    try:
        with open(USERS_FILE, mode="r", encoding="utf-8") as file:
            users = csv.DictReader(file)
            for u in users:
                if u["username"] == username and u["password_hash"] == hash_pw:
                    return username
    except Exception as e:
        print(f"Błąd logowania: {e}")
    return None
