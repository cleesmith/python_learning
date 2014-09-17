# pip install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector
cnx = mysql.connector.connect(user='', password='',
                              host='',
                              database='')
cnx.close()
