import weather
import sender


# read the emails.txt file
def get_emails():
    emails={}
    try:
        email_file=open("emails.txt","r")
        for line in email_file:
            (email,name)=line.split(",")
            emails[email]=name.strip()
    except FileNotFoundError:
        print("Error")
    return emails


# read schedule.txt file
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


# call main function
main()
