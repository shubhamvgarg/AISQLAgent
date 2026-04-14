import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# ----------------------
# Create Tables
# ----------------------

cursor.executescript("""
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS order_items;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    city TEXT,
    created_at TEXT
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category_id INTEGER,
    price REAL,
    stock INTEGER,
    FOREIGN KEY(category_id) REFERENCES categories(id)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    total_amount REAL,
    status TEXT,
    created_at TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    price REAL,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);
""")

# ----------------------
# Insert Dummy Data
# ----------------------

# Users
users = [
    ("Alice", "alice@example.com", "New York"),
    ("Bob", "bob@example.com", "Los Angeles"),
    ("Charlie", "charlie@example.com", "Chicago"),
    ("David", "david@example.com", "Houston"),
    ("Eve", "eve@example.com", "Seattle")
]

for u in users:
    cursor.execute(
        "INSERT INTO users (name, email, city, created_at) VALUES (?, ?, ?, ?)",
        (*u, datetime.now().isoformat())
    )

# Categories
categories = ["Electronics", "Clothing", "Home", "Sports", "Books"]

for c in categories:
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (c,))

# Products
products = [
    ("Laptop", 1, 1200, 10),
    ("Phone", 1, 800, 20),
    ("T-Shirt", 2, 20, 100),
    ("Jeans", 2, 50, 60),
    ("Blender", 3, 70, 30),
    ("Sofa", 3, 500, 5),
    ("Football", 4, 25, 40),
    ("Tennis Racket", 4, 150, 15),
    ("Novel", 5, 15, 80),
    ("Notebook", 5, 5, 200)
]

for p in products:
    cursor.execute(
        "INSERT INTO products (name, category_id, price, stock) VALUES (?, ?, ?, ?)",
        p
    )

# Orders + Order Items
statuses = ["pending", "completed", "cancelled"]

for i in range(20):
    user_id = random.randint(1, 5)
    created_at = datetime.now() - timedelta(days=random.randint(0, 30))
    status = random.choice(statuses)

    cursor.execute(
        "INSERT INTO orders (user_id, total_amount, status, created_at) VALUES (?, ?, ?, ?)",
        (user_id, 0, status, created_at.isoformat())
    )

    order_id = cursor.lastrowid

    total = 0
    for _ in range(random.randint(1, 3)):
        product_id = random.randint(1, 10)
        quantity = random.randint(1, 5)

        cursor.execute("SELECT price FROM products WHERE id=?", (product_id,))
        price = cursor.fetchone()[0]

        total += price * quantity

        cursor.execute(
            "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)",
            (order_id, product_id, quantity, price)
        )

    cursor.execute(
        "UPDATE orders SET total_amount=? WHERE id=?",
        (total, order_id)
    )

conn.commit()
conn.close()

print("✅ Dummy e-commerce database created!")