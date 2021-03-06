import socket
import datetime

HOST = '192.168.0.2'
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(ADDR)
serv.listen(5)
print('listening ...')
while True:
  conn, addr = serv.accept()
  print('client connected ... ', addr)
  filename = '/Users/auser/Sites/python/picamera/images/img_' + \
    datetime.datetime.now().strftime('%Y-%m-%dT%H.%M.%S.%f') + '.jpg'
  # create and open file for writing:
  myfile = open(filename, 'w')

  while True:
    data = conn.recv(BUFSIZE)
    if not data: break
    myfile.write(data)

  myfile.close()
  print('finished writing file: ', filename)
  conn.close()
  print('client disconnected')
