# pip install mysql-connector-python --allow-external mysql-connector-python

import datetime
import mysql.connector
config = {
  'user': '',
  'password': '',
  'host': '',
  'database': '',
  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
query = ("SELECT name, query, es_search, updated_at FROM searches")
cursor.execute(query)
for (name, query, es_search, updated_at) in cursor:
  print("updated_at={} name={} query={}\nes_search={}".format(updated_at, name, query, es_search))
  print('_'*80)
cursor.close()
cnx.close()
