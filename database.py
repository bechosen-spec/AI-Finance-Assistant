import sqlite3


def get_connection():
    return sqlite3.connect(
        "expenses.db",
        check_same_thread=False
    )


def create_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        description TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_expense(
    amount,
    category,
    description,
    date
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses
    (amount, category, description, date)
    VALUES (?, ?, ?, ?)
    """,
    (
        amount,
        category,
        description,
        date
    ))

    conn.commit()
    conn.close()


def get_expenses():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM expenses
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data