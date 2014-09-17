import email.message, email.mime.text, smtplib, sys
from email.utils import parseaddr, formataddr
from email.header import Header
from email.charset import Charset

def format_address(name, email):
  if not name:
    return email
  name = Charset('iso-8859-1').header_encode(name)
  return formataddr((name, email))

def send_unicode_email(mFrom, mTo, mSubject, mBody):
  sender_name, sender_addr = parseaddr(mFrom)
  recipient_name, recipient_addr = parseaddr(mTo)

  composed = email.mime.text.MIMEText(mBody.encode('UTF-8'), _charset='UTF-8')
  composed['from'] = format_address(sender_name, sender_addr)
  composed['to'] = format_address(recipient_name, recipient_addr)
  composed['subject'] = Header(mSubject, 'UTF-8')

  srv = smtplib.SMTP('localhost')
  srv.send_message(composed)
  srv.quit()
