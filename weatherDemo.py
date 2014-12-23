import  pywapi
import string

weather_com_result = pywapi.get_weather_from_weather_com('10001')

filename = raw_input('Please enter a zipcode: ')
yahoo_result = pywapi.get_weather_from_yahoo(filename)
noaa_result = pywapi.get_weather_from_noaa('KJFK')

# print "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in New York.\n\n"

print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "C now in New York.\n\n"
print "this is the city : " + string.lower(yahoo_result['location']['city'])
# print "NOAA says: It is " + string.lower(noaa_result['weather']) + " and " + noaa_result['temp_c'] + "C now in New York.\n"