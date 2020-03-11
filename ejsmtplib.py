import smtplib
to = "isaura.r29@gmail.com"
gmail_user = "isaura.rs29@gmail.com"
gmail_pwd = "Irs290797"
smtpserver = smtplib.SMTP("smtp.gmail.com")
smtpserver.starttls()
smtpserver.login(gmail_user,gmail_pwd)
header = 'To: ' + '\n' + 'Format' + gmail_user + '\n' + 'Subject:Python smtp\n'
print(header)
msg=header + '\n Hola'
print(smtpserver.sendmail(gmail_user,to,msg))
print('Enviado')
smtpserver.close()
