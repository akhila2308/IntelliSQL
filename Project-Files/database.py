import sqlite3

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS STUDENTS(
        NAME TEXT,
        CLASS TEXT,
        MARKS INTEGER,
        COMPANY TEXT
    );
    """)

    cursor.execute("DELETE FROM STUDENTS")

    sample_data = [
        ("Sita", "BTech", 85, "INFOSYS"),
        ("Ram", "MTech", 78, "TCS"),
        ("Shibin", "MSc", 90, "INFOSYS"),
        ("Riya", "BSc", 88, "WIPRO"),
        ("Diya", "MCom", 92, "EY"),
    ]

    cursor.executemany("INSERT INTO STUDENTS VALUES (?, ?, ?, ?)", sample_data)

    conn.commit()
    conn.close()


def read_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

