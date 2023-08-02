import requests

response = requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
json_resp = response.json()
x = int(input("enter the number of your choice"))
resp_1 = json_resp['list'][x]['weather'][0]
resp_2 = json_resp['list'][x]['wind']['speed']
resp_3 = json_resp['list'][x]['main']['pressure']
resp_4 = "Exit"

number = int(input("enter the number option"))

if number == 1:
    print(resp_1)
elif number == 2:
    print(resp_2)
elif number == 3:
    print(resp_3)
elif number == 0:
    print(resp_4)
else:
    print("invalid response number")



