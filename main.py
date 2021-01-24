import mysql.connector
import sqlalchemy as db

# SQL
my_db = mysql.connector.connect(host="localhost", user="root", password="Aa123456", database="store-medium")

my_cursor = my_db.cursor()

print("describe category")
my_cursor.execute("describe category")
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)

print("SELECT")
my_cursor.execute("SELECT * FROM category")
my_result = my_cursor.fetchall()
for x in my_result:
    print(x)

# SP
print('Store procedure')
my_cursor.callproc("store.new_procedure")
for result in my_cursor.stored_results():
    print(result.fetchall())

# ORM
engine = db.create_engine('mysql+pymysql://root:Aa123456@localhost/store-medium')
connection = engine.connect()
metadata = db.MetaData()
category = db.Table('category', metadata, autoload=True, autoload_with=engine)
print(category.columns.keys())
# same as "SELECT * FROM category"
query = db.select([category])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)

# SP
print('Store procedure')
connection = engine.raw_connection()
cursor = connection.cursor()
cursor.callproc("store.new_procedure")
results = list(cursor.fetchall())
print(results)
