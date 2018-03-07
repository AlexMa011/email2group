#!/usr/local/bin/python
"""A script for sending specialized emails to group
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# config email
from_addr = ''
cc_addr = ''
passwd = ''
mail_server_addr = 'mail.sjtu.edu.cn'
mail_server_port = 465
# the contacts list
list_file = 'list.txt'
# the email body
msg_subject = ''
msg_body = ''' '''

# retrive contacts list
f = open(list_file, 'r')
lists = []
for line in f.readlines():
    strings = line.split()
    email = strings[0]
    name = ''
    for surname in strings[1:]:
        name += surname
        name += ' '
    lists.append([email, name[:-1]])

server = smtplib.SMTP_SSL(mail_server_addr, mail_server_port)
server.login(from_addr, passwd)

for email_name in lists:
    email = email_name[0]
    name = email_name[1]

    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = email
    msg['Cc'] = cc_addr
    msg['Subject'] = msg_subject

    # write speciliazed email
    body = 'Dear ' + name + ',' + msg_body

    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail(from_addr, [toaddr, cc_addr], text)

server.quit()
