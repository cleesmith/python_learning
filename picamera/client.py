import socket
HOST = '192.168.0.2'
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096
# videofile = "videos/royalty-free_footage_wien_18_640x360.mp4"
# bytes = open(videofile).read()
# print len(bytes)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.send(bytes)
client.close()
