import pymysql.cursors
import pandas as pd

SERVER_URL = "localhost"
DB = "usms"
USER_NAME = "root"
PASSWORD = "root"
CSV_FIlE = "./hotel_bookings.csv"

connection = pymysql.connect(host=SERVER_URL,
                             user=USER_NAME,
                             passwd=PASSWORD,
                             db=DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=True)

csv = pd.read_csv(CSV_FIlE)
print(csv.info())
print(dict(csv.dtypes))

