import pandas as pd
from sqlalchemy import create_engine

CSV_FILE = './hotel_bookings.csv'
DATABASE_TYPE = 'mysql'
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'demo'
TABLE = 'demo_hotel'
HOST = 'localhost'

DB_URL = DATABASE_TYPE + "+pymysql://" + USERNAME + ":" + PASSWORD + "@" + HOST + "/" + DATABASE

df = pd.read_csv(CSV_FILE)
engine = create_engine(DB_URL, pool_recycle=3600)

with engine.connect() as conn, conn.begin():
    try:
        df.to_sql(TABLE, conn, if_exists='replace', index=False)
    except Exception as err:
        print(err.__cause__)
    finally:
        print("CSV successfully imported")
