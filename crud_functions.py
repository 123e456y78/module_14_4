import sqlite3
def initiate_db():
    connection = sqlite3.connect('data_products1.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    )
    ''')
    connection.commit()
    connection.close()
initiate_db()
def insert_products():
    connection = sqlite3.connect('data_products1.db')
    cursor = connection.cursor()
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       (f"Продукт {i}", f"Описание {i}", i*100))
    connection.commit()
    connection.close()
insert_products()
def delete_records():
    connection = sqlite3.connect('data_products1.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Products WHERE id BETWEEN 5 AND 16")
    connection.commit()
    connection.close()
delete_records()
def get_all_products():
    connection = sqlite3.connect('data_products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    for product in products:
        id, title, description, price = product
        print(f"ID: {id} | Наименование: {title} | Описание: {description} | Цена: {price}")
    connection.commit()
    connection.close()
    return products
get_all_products()
# connection.commit()
# connection.close()