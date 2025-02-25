import sqlite3

# Function to initialize database and create tables
def init_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Create table for storing product details
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            serial TEXT UNIQUE NOT NULL,
            owner TEXT NOT NULL
        )
    ''')

    # Create table for tracking product scans
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            serial TEXT NOT NULL,
            scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("[✅] Database initialized successfully!")

# Function to add a new product
def add_product(name, serial, owner):
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, serial, owner) VALUES (?, ?, ?)", (name, serial, owner))
        conn.commit()
        conn.close()
        return {"status": "success", "message": "Product added successfully"}
    except sqlite3.IntegrityError:
        return {"status": "error", "message": "Product with this serial already exists"}

# Function to check if a product exists
def check_product(serial):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE serial = ?", (serial,))
    product = cursor.fetchone()
    conn.close()
    return product is not None

# Function to log QR code scan
def log_scan(serial):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scans (serial) VALUES (?)", (serial,))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Scan logged successfully"}

# Initialize the database
if __name__ == "__main__":
    init_db()
