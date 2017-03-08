import requests


# get the weather forecast in Lonodn
def get_weather_forecast():
	url='http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&&APPID=5e1d8efd49bb21e6a6c3d0edede0563d'
	weather_request=requests.get(url)
	weather_json=weather_request.json()


	description = weather_json["weather"][0]["description"]
	temp_min = weather_json["main"]["temp_min"]
	temp_max = weather_json["main"]["temp_max"]


	forecast = "The Forecast for Today is "
	forecast += description + ' with a high of ' + str(int(temp_max)) + ' Celsius degree'
	forecast += ' and a low of ' + str(int(temp_min)) + ' Celsius degree'
	return forecast
