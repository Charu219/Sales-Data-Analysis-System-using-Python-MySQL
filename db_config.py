import os
import mysql.connector
from urllib.parse import urlparse

def get_connection():
    url = urlparse(os.getenv("MYSQL_URL"))
    return mysql.connector.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path[1:],
        port=url.port or 3306
    )





# import os
# import mysql.connector

# def get_connection():
#     return mysql.connector.connect(
#         host=os.getenv("MYSQLHOST"),
#         user=os.getenv("MYSQLUSER"),
#         password=os.getenv("MYSQLPASSWORD"),
#         database=os.getenv("MYSQLDATABASE"),
#         port=int(os.getenv("MYSQLPORT"))
#     )









# import os

# host = os.getenv("MYSQLHOST")
# user = os.getenv("MYSQLUSER")
# password = os.getenv("MYSQLPASSWORD")
# database = os.getenv("MYSQLDATABASE")







# import mysql.connector

# def get_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Charu@060905",
#         database="sales_db"
#     )
