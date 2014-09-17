# pip install mysql-connector-python --allow-external mysql-connector-python

import datetime
import mysql.connector
config = {
  'user': '',
  'password': '',
  'host': '',
  'database': 'snort',
  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# query:
# query = ("SELECT sig_id, sig_name FROM signature")
# cursor.execute(query)
# for (sig_id, sig_name) in cursor:
#   print("id=%s\tname=%s" % (sig_id, sig_name))
#   # print('_'*80)

# insert:
# data = [
#   ('Jane', datetime.datetime.now()),
#   ('Joe', datetime.datetime.now()),
#   ('John', datetime.datetime.now()),
# ]
# print(type(data))

map = {}
entry = {
    "msg": "this is msg 456",
    "gid": 123,
    "sid": 456,
    "ref": "ref 1"
}
map[123, 456] = entry
entry = {
    "msg": "this is msg 333",
    "gid": 333,
    "sid": 333,
    "ref": "ref 333"
}
map[333, 333] = entry
print(type(map))
print(map)
entry_list = list(map.values())
print(type(entry_list))
print(entry_list)

stmt = "INSERT INTO _cls (gid, sid, msg, ref) VALUES (%(gid)s, %(sid)s, %(msg)s, %(ref)s)"
cursor.executemany(stmt, entry_list)
cnx.commit()

cursor.close()
cnx.close()
