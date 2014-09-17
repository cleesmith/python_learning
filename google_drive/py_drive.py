from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

f = drive.CreateFile()
f.SetContentFile('document.txt')
f.Upload()
print('title: %s, mimeType: %s' % (f['title'], f['mimeType']))

# f = drive.CreateFile({'title': 'Hello.txt'})
# f.SetContentString('Hello World!')
# f.Upload()

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
