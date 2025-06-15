import sqlite3
from datetime import datetime

# --- Connect to SQLite ---
def get_connection():
    return sqlite3.connect("bank.db")

# --- Create Tables ---
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            balance REAL DEFAULT 0
        )
    """)

    # Create transactions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            type TEXT,
            amount REAL,
            time TEXT
        )
    """)

    conn.commit()
    conn.close()
    print(" Tables created.")

# --- Register User ---
def register_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        print(" Registered successfully.")
    except:
        print("❌ Email already registered.")
    conn.close()

# --- Login User ---
def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Login successful.")
        return user[0]
    else:
        print("❌ Login failed.")
        return None

# --- Deposit or Withdraw ---
def transaction(user_id, type_, amount):
    conn = get_connection()
    cursor = conn.cursor()

    # Get current balance
    cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
    balance = cursor.fetchone()[0]

    # Check if enough balance
    if type_ == "withdraw" and balance < amount:
        print("❌ Not enough balance.")
        conn.close()
        return

    # Update balance
    new_balance = balance + amount if type_ == "deposit" else balance - amount
    cursor.execute("UPDATE users SET balance=? WHERE id=?", (new_balance, user_id))

    # Log transaction
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO transactions (user_id, type, amount, time) VALUES (?, ?, ?, ?)",
                   (user_id, type_, amount, time))

    conn.commit()
    conn.close()
    print(f"✅ {type_.capitalize()} successful. New balance: {new_balance}")

# --- Check Balance ---
def check_balance(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,))
    balance = cursor.fetchone()[0]
    conn.close()
    print(f"💰 Balance: {balance}")

# --- Main: Run once to create tables ---
if __name__ == "__main__":
    create_tables()

    # Sample usage (uncomment to try):
    # register_user("Hiba", "hiba@mail.com", "123")
    # uid = login_user("hiba@mail.com", "123")
    # if uid:
    #     transaction(uid, "deposit", 500)
    #     transaction(uid, "withdraw", 200)
    #     check_balance(uid)