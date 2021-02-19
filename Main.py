import requests, json

dSign= u'\N{DEGREE SIGN}'

def GetWeather():
  City = input('Enter City: ').capitalize()
  API_Key = 'c582baae2211b7a4266ac723b9bb39d8'
  MainURL = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format(City,API_Key)
  Requesting = requests.get(MainURL)
  if Requesting.status_code == 200:
    data = Requesting.json()
    #print(data)
    MainData = data['main']
    WindData = data['wind']
    temp = str(MainData['temp'])
    press = MainData['pressure']
    feels_like = str(MainData['feels_like'])
    humidity = str(MainData['humidity'])
    WindSpeed = WindData['speed']
    pc = City,'Current Weather Forecast:'
    print('\n','\033[4m',City,'Current Weather Forecast:','\033[0m')
    print('\n',
    'Temperature: ',temp+dSign+'F','\n',
    'Feels Like: ',feels_like+dSign+'F','\n',
    'Humidity: ',humidity+'%','\n',
    'Wind Speed: ',WindSpeed,'mph','\n',
    'Barometric Pressure: ',press,'millibar','\n'
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
