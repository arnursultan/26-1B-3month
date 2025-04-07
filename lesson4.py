# import sqlite3
#
# def connect():
#     return sqlite3.connect('products.db')
#
# def create_table():
#     conn = connect()
#     cursor = conn.cursor()
#
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS products (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         price INTEGER NOT NULL,
#         quantity INTEGER NOT NULL
#     )
#     """)
#     conn.commit()
#     conn.close()
#     print("Таблица products успешно создана!")
#
# def add_product(name, price, quantity):
#     try:
#         conn = connect()
#         cursor = conn.cursor()
#         cursor.execute("""
#         INSERT INTO products (name, price, quantity)
#         VALUES (?, ?, ?)
#         """,(name, price, quantity))
#         conn.commit()
#         print(f"Товар '{name}' успешно добавлен!")
#     except sqlite3.Error as e:
#         print(f"Ошибка при получении данных: {e}")
#     finally:
#         conn.close()
#
# def show_products():
#     try:
#         conn = connect()
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM products')
#         rows = cursor.fetchall()
#         conn.close()
#
#         if rows:
#             print("Список товаров в базе данных:")
#             for row in rows:
#                 print(f"ID: {row[0]}, Название: {row[1]}, Цена: {row[2]}, Количество: {row[3]}")
#         else:
#             print("Нет товаров в базе данных.")
#     except sqlite3.Error as e:
#         print(f"Ошибка при получении данных: {e}")
#
# def update_product(product_id, price, quantity):
#     try:
#         conn = connect()
#         cursor = conn.cursor()
#         cursor.execute('''
#         UPDATE products
#         SET price = ?, quantity = ?
#         WHERE id = ?
#         ''', (price, quantity, product_id))
#         conn.commit()
#
#         if cursor.rowcount > 0:
#             print(f"Данные товара с ID {product_id} успешно обновлены!")
#         else:
#             print(f"Товар с ID {product_id} не найден.")
#
#     except sqlite3.Error as e:
#         print(f"Ошибка при получении данных: {e}")
#     finally:
#         conn.close()
#
# def delete_product(product_id):
#     try:
#         conn = connect()
#         cursor = conn.cursor()
#         cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
#         conn.commit()
#
#         if cursor.rowcount > 0:
#             print(f"Товар с ID {product_id} успешно удален!")
#         else:
#             print(f"Товар с ID {product_id} не найден.")
#     except sqlite3.Error as e:
#         print(f"Ошибка при получении данных: {e}")
#     finally:
#         conn.close()
#
# def add_secure_product(name, price, quantity):
#     try:
#         conn = connect()
#         cursor = conn.cursor()
#         cursor.execute("""
#         INSERT INTO products (name, price, quantity)
#         VALUES (?, ?, ?)
#         """, (name, price, quantity))
#         conn.commit()
#         print("Безопасно добавлен товар с '{name'!")
#     except sqlite3.Error as e:
#         print(f"Ошибка при получении данных: {e}")
#     finally:
#         conn.close()
#
# def execute_query(query, params=()):
#     try:
#         conn = connect()
#         cursor = conn.cursor()
#         cursor.execute(query, params)
#         conn.commit()
#         return cursor
#     except sqlite3.Error as e:
#         print(f"Ошибка при получении данных: {e}")
#     finally:
#         conn.close()
#
# def main():
#     create_table()
#
#     while True:
#         print("\n=========================")
#         print("Управление товарами")
#         print("=========================")
#         print("1 Добавить новый товар")
#         print("2 Показать все товары")
#         print("3 Обновить информацию о товаре")
#         print("4 Удалить товар")
#         print("5 Выйти")
#
#         choice = input("Введите номер действия: ")
#
#         if choice == "1":
#             name = input("Введите название товара: ")
#             price = float(input("Введите цену товара: "))
#             quantity = int(input("Введите количество товара: "))
#             add_product(name, price, quantity)
#
#         elif choice == "2":
#             show_products()
#
#         elif choice == "3":
#             product_id = int(input("Введите ID товара для обновления: "))
#             price = float(input("Введите новую цену: "))
#             quantity = int(input("Введите новое количество: "))
#             update_product(product_id, price, quantity)
#
#         elif choice == "4":
#             product_id = int(input("Введите ID товара для удаления: "))
#             delete_product(product_id)
#
#         elif choice == "5":
#             print("Выход из программы...")
#             break
#
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#
# if __name__ == "__main__":
#     main()

