import os
pwd = os.getcwd()
print(pwd)
os.mkdir('newdir')

import time
time.sleep(2)
os.rename('newdir', 'newdir2')
time.sleep(2)
os.rmdir('newdir2')

