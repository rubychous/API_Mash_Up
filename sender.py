import smtplib
# sending an email
def send_emails(emails,schedule,forecast):
	
	# connect to the smpt server
	server = smtplib.SMTP('smtp.gmail.com','587')

	# start TLS encryption
	server.starttls()

	# Login
	Password=input("what's your password: ")
	from_email = "rubychous@gmail.com"
	server.login(from_email,Password)

	# send to entire email list
	for to_email in emails:
		message = 'Subject: Hi\n'
		message += 'Hello!!:\n\n'
		message += forecast+'\n\n'
		message += schedule+'\n\n'
		message += 'Hope to see u there!'
		server.sendmail(from_email,from_email,message)
	server.quit()