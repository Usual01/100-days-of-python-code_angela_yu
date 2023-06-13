import requests

api_key = ""
# MY_LAT = 6.524379
# MY_LONG = 3.379206

OWM = "https://api.openweathermap.org/data/2.5/onecall"
w_params = {
    "lat":6.524379,
    "lon": 3.379206,
    "appid": api_key,

}

response = requests.get(OWM, params=w_params)
print(response.status_code)
