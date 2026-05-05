from flask import Flask, render_template, request, redirect, url_for

from db_config import get_connection
from datetime import date

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        product = request.form["product"]
        quantity = request.form["quantity"]
        price = request.form["price"]

        cursor.execute(
            "INSERT INTO sales (product_name, quantity, price, sale_date) VALUES (%s,%s,%s,%s)",
            (product, quantity, price, date.today())
        )
        conn.commit()

    cursor.execute("SELECT * FROM sales")
    sales = cursor.fetchall()

    cursor.execute("SELECT SUM(quantity * price) FROM sales")
    revenue = cursor.fetchone()[0]

    conn.close()

    return render_template("index.html", sales=sales, revenue=revenue)




@app.route("/delete/<int:sale_id>")
def delete_sale(sale_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sales WHERE id = %s", (sale_id,))
    conn.commit()

    conn.close()
    return redirect(url_for("index"))











if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)









































# from db_config import get_connection
# from datetime import date

# conn = get_connection()
# cursor = conn.cursor()

# def insert_sale(product, quantity, price):
#     sql = "INSERT INTO sales (product_name, quantity, price, sale_date) VALUES (%s,%s,%s,%s)"
#     values = (product, quantity, price, date.today())
#     cursor.execute(sql, values)
#     conn.commit()
#     print("Sale inserted")

# def show_all_sales():
#     cursor.execute("SELECT * FROM sales")
#     for row in cursor.fetchall():
#         print(row)

# def total_revenue():
#     cursor.execute("SELECT SUM(quantity * price) FROM sales")
#     print("Total Revenue:", cursor.fetchone()[0])

# def top_product():
#     cursor.execute("""
#         SELECT product_name, SUM(quantity) AS total_qty
#         FROM sales
#         GROUP BY product_name
#         ORDER BY total_qty DESC
#         LIMIT 1
#     """)
#     print("Top Product:", cursor.fetchone())

# # -------- MENU ----------
# while True:
#     print("\n1.Insert Sale\n2.View Sales\n3.Total Revenue\n4.Top Product\n5.Exit")
#     choice = input("Enter choice: ")

#     if choice == "1":
#         p = input("Product: ")
#         q = int(input("Quantity: "))
#         pr = float(input("Price: "))
#         insert_sale(p, q, pr)

#     elif choice == "2":
#         show_all_sales()

#     elif choice == "3":
#         total_revenue()

#     elif choice == "4":
#         top_product()

#     elif choice == "5":
#         break

# conn.close()
