# none of this works!
import httplib2
import urllib
import sys
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# email of the Service Account:
# SERVICE_ACCOUNT_EMAIL = ''
SERVICE_ACCOUNT_EMAIL = ''
# path to the Service Account's Private Key file:
SERVICE_ACCOUNT_PKCS12_FILE_PATH = 'detect motion-02d3a74bbb95.p12'

def createDriveService():
  f = file(SERVICE_ACCOUNT_PKCS12_FILE_PATH, 'rb')
  key = f.read()
  f.close()

  credentials = SignedJwtAssertionCredentials(SERVICE_ACCOUNT_EMAIL, key,
      scope="https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/drive.file"
  )
  http = httplib2.Http()
  http = credentials.authorize(http)
  # return build('drive', 'v2', http=http)
  return credentials

# gauth = GoogleDrive()
# gauth.credentials = createDriveService()
# drive = GoogleDrive(gauth)

f = file(SERVICE_ACCOUNT_PKCS12_FILE_PATH, 'rb')
key = f.read()
f.close()

# no work:
# http = httplib2.Http()
# body = {'approval_prompt':'force'}
# response, content = http.request('https://accounts.google.com/o/oauth2/auth?client_id=202406790888-1s6kihv5lmo8leqkbqamgl651sucotan.apps.googleusercontent.com&scope=https://www.googleapis.com/auth/drive&response_type=code&approval_prompt=force', 'GET')
# print(response)

credentials = SignedJwtAssertionCredentials(SERVICE_ACCOUNT_EMAIL, key,
    scope="https://www.googleapis.com/auth/drive"
)
credentials.authorize(httplib2.Http())
gauth = GoogleAuth()
gauth.credentials = credentials
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
