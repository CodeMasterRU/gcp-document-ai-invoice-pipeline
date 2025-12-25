import sqlite3

def load_to_db(data):
    conn = sqlite3.connect("database/invoices.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            invoice_number TEXT,
            invoice_date TEXT,
            supplier TEXT,
            total_amount REAL,
            currency TEXT,
            vat REAL
        )
    """)

    cur.execute("""
        INSERT INTO invoices VALUES (?, ?, ?, ?, ?, ?)
    """, tuple(data.values()))

    conn.commit()
    conn.close()