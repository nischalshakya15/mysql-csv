## mysql-csv 
A simple command line utility which helps to export the csv file directly into database without a hassle to create a table 
and specify a data type. 

## Purpose
It is created solely for the purpose to help data analyst for the data manipulation and getting the result using an sql query 
which in turns help analyst to get the required information before hand. This information will help analyst to expect what type of information 
should a data frame hold for data visualization.

## Prerequisites 
* python 
* pip 
* pandas
* numpy 
* SQLAlchemy
* setup-tools

## Help
View the usage of command line parameters.

``python mysql-csv.py --help`` 

```
usage: mysql-csv.py [-h] [--hostname] --file [--database] [--database-type] [--username] [--password] [--table] [--dialect]

optional arguments:
  -h, --help         show this help message and exit
  --hostname       domain name or ip address of database
  --file           csv file to be exported to table
  --database       database name
  --database-type  database type mysql | sql | oracle | postgres
  --username       username of database
  --password       password of database
  --table          table where csv to be imported
  --dialect        database dialect pymysql for mysql
```

## Import csv file into database
```
python mysql-csv.py --hostname localhost --file hotel_bookings.csv --database demo --database-type mysql --username root --password root --table=something --dialect pymysql
```