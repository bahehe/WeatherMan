import requests, json

def GetWeather():
  City = input('Enter City: ').capitalize()
  API_Key = 'c582baae2211b7a4266ac723b9bb39d8'
  MainURL = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format(City,API_Key)
  Requesting = requests.get(MainURL)
  if Requesting.status_code == 200:
    data = Requesting.json()
    print(data)
    MainData = data['main']
    WindData = data['wind']
    temp = MainData['temp']
    feels_like = MainData['feels_like']
    humidity = MainData['humidity']
    WindSpeed = WindData['speed']

    print(
    '\n',City,'Current Weather Forecast:','\n',
    'Temperature: ',temp,'F','\n',
    'Feels Like: ',feels_like,'F','\n',
    'Humidity: ',humidity,'%','\n',
    'Wind Speed: ',WindSpeed,'mph','\n',
    )
  else:
    print('Invalid City.')
    GetWeather()
def Repeat():
  repeat = input('Repeat? (y/n): ').upper()
  if repeat == 'Y':
    GetWeather()
  elif repeat == 'N':
    exit()
  else:
    Repeat()
GetWeather()
Repeat()
 
