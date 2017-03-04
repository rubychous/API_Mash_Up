# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:13:20 2017

@author: LUYI
"""
import requests
def get_weather_forecast():
	url='http://api.openweathermap.org/data/2.5/weather?q=London&APPID=yourapikey'
	weather_request=requests.get(url)
	weather_json=weather_request.json()


	description = weather_json["weather"][0]["description"]
	temp_min = weather_json["main"]["temp_min"]
	temp_max = weather_json["main"]["temp_max"]


	forecast = "The Forecast for Today is "
	forecast += description + ' with a high of ' + str(int(temp_max))
	forecast += ' and a low of ' + str(int(temp_min))
	return forecast
