from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
# try to load saved client credentials
gauth.LoadCredentialsFile("creds_detect_motion.txt")
if gauth.credentials is None:
    # authenticate if they're not there
    print('using LocalWebserverAuth ...')
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # refresh them if expired
    print('refresh creds ...')
    gauth.Refresh()
else:
    # initialize the saved creds
    print('using Authorize ...')
    gauth.Authorize()
# save the current credentials to a file
gauth.SaveCredentialsFile("creds_detect_motion.txt")

drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
