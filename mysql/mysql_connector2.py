import mysql.connector

config = {
  'user': '',
  'password': '',
  'host': '',
  'database': '',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)

cnx.close()
