import os, json, urllib.request 

f = open(os.path.dirname(__file__)+'/clear.txt','r')
clear = f.read()
f.close()
f = open(os.path.dirname(__file__)+'/clouds.txt','r')
clouds = f.read()
f.close()
f = open(os.path.dirname(__file__)+'/drizzle.txt','r')
drizzle = f.read()
f.close()
f = open(os.path.dirname(__file__)+'/rain.txt','r')
rain = f.read()
f.close()
f = open(os.path.dirname(__file__)+'/default.txt','r')
default = f.read()
f.close()

try: 
    URL = "http://api.openweathermap.org/data/2.5/weather?zip=30318,us&units=metric&appid=d54cd01e8005bc84825fce37ff2d073a"
    req = urllib.request.Request(URL)
    response = urllib.request.urlopen(req).read()
    data = json.loads(response)

    print('\033[1;32;49m\nToday\'s weather:')
    weather = str(data['weather'][0]['main'])
    if weather == 'Clear':
        print('\033[1;33;49m\n' + clear)
    elif weather == 'Clouds':
        print('\033[1;33;49m\n' + clouds)
    elif weather == 'Drizzle':
        print('\033[1;34;49m\n' + drizzle)
    elif weather == 'Rain' or weather == 'Snow':
        print('\033[1;34;49m\n' + rain)
    else:
        print('\033[1;34;49m\n' + default)

    print('\033[1;32;49m\t\t' + str(int(data['main']['temp'])) + '°C', '|', str(data['weather'][0]['description']))
    print('\t   min:', str(data['main']['temp_min']) + '°C', '| max:', str(data['main']['temp_max']) + '°C\n')

except:
    print('No internet connection')
