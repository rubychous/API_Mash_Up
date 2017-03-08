import smtplib


def send_emails(emails,schedule,forecast):
	
	# connect to the smpt server
	server = smtplib.SMTP('smtp.gmail.com','587')
	server.ehlo()

	# start TLS encryption
	server.starttls()

	# Login
	#Password=input("what's your password: ")
	#from_email = "rubychous@gmil.com"
	server.login("rubychous@gmil.com","2016BIGdata")

	# send to entire email list
	for to_email,name in emails.items():
		message = 'Subject: Weather Forecast and ToDo List \n'
		message += 'Hello!! '+ name + ' :\n\n'
		message += forecast+'\n\n'
		message += schedule+'\n\n'
		message += 'Have a Nice Day!'
		server.sendmail("rubychous@gmil.com","sweetywish35@gmail.com",message)
	server.quit()