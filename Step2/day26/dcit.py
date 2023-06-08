"""
you are going to use dictionary Comprehension to create a dictionary
called weather_r that takes temperature in degree celsius 
and converts it to farenheight

"""
weather_c = {
    "Monday": 12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday":24,
}

weather_f = {day: temp *9/5 +32 for (day, temp) in weather_c.items()}
print(weather_f)