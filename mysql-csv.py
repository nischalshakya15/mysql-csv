import argparse

import pandas as pd
from sqlalchemy import create_engine

parser = argparse.ArgumentParser()
parser.add_argument("--hostname", dest="hostname", metavar="\b", default="localhost",
                    help='domain name or ip address of database')
parser.add_argument("--file", type=str, dest="csv_file", metavar="\b", required=True,
                    help="csv file to be exported to table")
parser.add_argument("--database", type=str, dest="database", metavar="\b", required=True, help="database name")
parser.add_argument("--database-type", type=str, dest="database_type", metavar="\b", required=True,
                    help="database type mysql | sql | oracle | postgres")
parser.add_argument("--username", type=str, dest="username", metavar="\b", required=True, help="username of database")
parser.add_argument("--password", type=str, dest="password", metavar="\b", required=True, help="password of database")
parser.add_argument("--table", type=str, dest="table", metavar="\b", required=True,
                    help="table where csv to be imported")
parser.add_argument("--dialect", type=str, dest="dialect", metavar="\b", required=True,
                    help="database dialect pymysql for mysql")
args = parser.parse_args()

CSV_FILE = args.csv_file
DATABASE_TYPE = args.database_type
USERNAME = args.username
PASSWORD = args.password
DATABASE = args.database
TABLE = args.table
HOST = args.hostname
DIALECT = args.dialect

DB_URL = DATABASE_TYPE + "+" + DIALECT + "://" + USERNAME + ":" + PASSWORD + "@" + HOST + "/" + DATABASE

try:
    df = pd.read_csv(CSV_FILE)
    engine = create_engine(DB_URL, pool_recycle=3600)
    with engine.connect() as conn, conn.begin():
        df.to_sql(TABLE, conn, if_exists='replace', index=False)
    print("CSV successfully imported")
except Exception as err:
    print(err.__cause__)
