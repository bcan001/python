from pandas.io import sql
import sqlite3

conn = sqlite3.connect('/Users/bencaneba/desktop/projects/vantech/db/development.sqlite3')
#query = "SELECT * FROM shipments WHERE user_id = 1;"
query = "SELECT shipper,consignee FROM shipments WHERE user_id = 1;"

results = sql.read_sql(query, con=conn)
print results.head()
print



# read your copy clipboard and convert into pandas
import pandas
clip = pandas.read_clipboard().head()
print clip
print