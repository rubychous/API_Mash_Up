import weather
import sender

def get_emails():
	try:
		email_file=read_csv("emails.csv")
		for line in range(0,2):
			emails = email_file.at[line,"email"]
	except FileNotFoundError:
		print("ERROR")
	return emails

# read schedule file
def get_schedule():
	try:
		schedule_file = open("schedule.txt","r")
		schedule = schedule_file.read()  # read a whole file
	except FileNotFoundError:
		print("ERROR")
	return schedule

# define main function
def main():
	emails=get_emails()
	schedule=get_schedule()
	forecast=weather.get_weather_forecast()
	sender.send_emails(emails,schedule,forecast)

main()