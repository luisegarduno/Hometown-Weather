import sys
import json
import time
import os.path
import subprocess

# Current working directory
cwd = os.path.dirname(os.path.realpath(__file__))

# Boolean flag that tells the program whether the user enabled text notifications
txt_notifs = True

os.system('cls' if os.name == 'nt' else 'clear')

# Check to see if program has been ran before 
if os.path.isfile('keys.oof') and os.path.isfile('weather-data.xlsx'):

    with open('keys.oof') as file:
        accuweather_api = file.readline()

        line = file.readline()
        line2 = file.readline()
        if line2 != '':
            account_sid = line
            auth_token = line2
            my_number = file.readline()
            twilio_number = file.readline()
            location_key = file.readline()
        else:
            location_key = line
            txt_notifs = False
    file.close()

else:
    print("Please wait while I check if you have all the necessary python modules \n")

    # implement pip as a subprocess & install necessary packages:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','xlrd', '-q'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','lxml', '-q'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','pandas', '-q'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','urllib3', '-q'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','requests', '-q'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','openpyxl', '-q'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','xlsxwriter', '-q'])

    # Print examples of accepted formatting for requested user input
    print("Okay, the necessary libraries have been downloaded")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    flag = True
    while flag:
        # Ask user if they would like text message notifications
        print("*Recommended*")
        txts = str(input("Would you like to enable txt-notifications? (y/n) : "))
        os.system('cls' if os.name == 'nt' else 'clear')

        if txts[0].lower() == 'y' or txts[0].lower() == 'n':
            creds = open("keys.oof", "w+")
            print("Let's get your credentials, here's some examples of the formatting ")
            print("     > [AccuWeather API] : AB1234a12a12a1234567a9a94573a1234a")
            print("     > [Postal/Zip Code] : 12345")

            if txts[0].lower() == 'y':
                print("     > [Account SID] : AB1234a12a12a1234567a9a94573a1234a")
                print("     > [Authentication Token] : AB1234a12a12a1234567a9a94573a1234a")
                print("     > [Personal Phone Number] : 9721231234")
                print("     > [TWILIO Phone Number] : 9721231234\n")
                print("** Need help? Check out the README (https://github.com/luisegarduno/MyWeather/blob/main/README.md)\n")

                print("Please enter the following information ")
                accuweather_api = str(input("     > [AccuWeather API] : "))
                creds.write(accuweather_api + "\n")

                search_code = str(input("     > [Postal/Zip Code] : "))
                params = (('apikey', accuweather_api), ('q', search_code), ('language', 'en-us'), ('details', 'true'))
                z_res = reqs.get('http://dataservice.accuweather.com/locations/v1/postalcodes/search', params=params)
                z_dict = json.loads(z_res.text)
                location_key = z_dict[0]['ParentCity']['Key']

                account_sid = str(input("     > [Account SID] : "))
                creds.write(account_sid + "\n")

                auth_token = str(input("     > [Authenticantion Token] : "))
                creds.write(auth_token + "\n")

                my_number = str(input("     > [Personal Phone Number] : "))
                creds.write(my_number + "\n")

                twilio_number = str(input("     > [TWILIO Phone Number] : "))
                creds.write(twilio_number + "\n")
                creds.write(location_key)

                print("Installing additional python modules...")
                subprocess.check_call([sys.executable, '-m', 'pip', 'install','twilio', '-q'])

                # Print introduction message & create file named 'secret.file'
                print("\n\nDone! Now if all the information is correct, program will start in a couple seconds :)")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                txt_notifs = True
                flag = False

            elif txts[0].lower() == 'n':
                print("** Need help? Check out the README (https://github.com/luisegarduno/MyWeather/blob/main/README.md)\n")

                print("Please enter the following information ")
                accuweather_api = str(input("     > [AccuWeather API] : "))
                creds.write(accuweather_api + "\n")

                import requests as reqs

                search_code = str(input("     > [Postal/Zip Code] : "))
                params = (('apikey', accuweather_api), ('q', search_code), ('language', 'en-us'), ('details', 'true'))
                z_res = reqs.get('http://dataservice.accuweather.com/locations/v1/postalcodes/search', params=params)
                z_dict = json.loads(z_res.text)
                location_key = z_dict[0]['ParentCity']['Key']
                creds.write(location_key)

                txt_notifs = False
                flag = False

            creds.close()

        else:
            print("Invalid Option. Try Again (Options: y OR n)")

    import xlsxwriter
    if os.path.isfile('weather-data.xlsx'):
        print('Continuing...')
    else:
        init_book = xlsxwriter.Workbook('weather-data.xlsx')
        init_book.close()

# -------------- Launch actual script now --------------- #
import json
import openpyxl
import xlsxwriter
import subprocess
import pandas as pd
import requests as reqs
from urllib.request import urlopen

weather_data = pd.read_excel('weather-data.xlsx')

os.system('cls' if os.name == 'nt' else 'clear')
print("*Weather*\n")

params = (('apikey', accuweather_api), ('language', 'en-us'), ('details', 'true'), ('metric', 'false'))

response_1 = reqs.get('http://dataservice.accuweather.com/forecasts/v1/daily/1day/' + str(location_key), params=params)
resp_dict1 = json.loads(response_1.text)

# Low Temperature
lo_unit = resp_dict1['DailyForecasts'][0]['Temperature']['Minimum']['Unit']
lo_temp = resp_dict1['DailyForecasts'][0]['Temperature']['Minimum']['Value']
lo = str(lo_temp) + lo_unit

# High Temperature
hi_unit = resp_dict1['DailyForecasts'][0]['Temperature']['Maximum']['Unit']
hi_temp = resp_dict1['DailyForecasts'][0]['Temperature']['Maximum']['Value']
hi = str(hi_temp) + hi_unit

# Wind (Speed / Direction)
wind_value = resp_dict1['DailyForecasts'][0]['Day']['Wind']['Speed']['Value']
wind_degrees = resp_dict1['DailyForecasts'][0]['Day']['Wind']['Direction']['Degrees']
wind_localized = resp_dict1['DailyForecasts'][0]['Day']['Wind']['Direction']['Localized']
wind = str(wind_value) + 'mph / ' + str(wind_degrees) + wind_localized

response_2 = reqs.get('http://dataservice.accuweather.com/currentconditions/v1/' + str(location_key), params=params)
resp_dict2 = json.loads(response_2.text)

# Pressure (Imperial)
pressure_value = resp_dict2[0]['Pressure']['Imperial']['Value']
pressure_unit = resp_dict2[0]['Pressure']['Imperial']['Unit']
pressure = str(pressure_value) + pressure_unit

# Precipitation
precipitation_value = resp_dict2[0]['PrecipitationSummary']['Precipitation']['Imperial']['Value']
precipitation_unit = resp_dict2[0]['PrecipitationSummary']['Precipitation']['Imperial']['Unit']
precipitation = str(precipitation_value) + precipitation_unit

# Humidity
relative_humidity = str(resp_dict2[0]['RelativeHumidity']) + '%'
indoor_relative_humidity = resp_dict2[0]['IndoorRelativeHumidity']

date_rn = time.strftime("%m/%d/%Y")

txt_2_me = 'Date : ' + str(date_rn)
txt_2_me += '\nLow Temperature : ' + lo
txt_2_me += '\nHi Temperature : ' + hi
txt_2_me += '\nPrecipitation : ' + precipitation
txt_2_me += '\nHumidity (Relative) : ' + relative_humidity
txt_2_me += '\nPressure : ' + pressure
txt_2_me += '\nWind (Speed/Direction) : ' + wind

print(txt_2_me + '\n')
line = date_rn + ',' + lo + ',' + hi + ',' + precipitation + ',' + relative_humidity + ',' + pressure + ',' + wind

weather_data2 = pd.DataFrame({'Date': [date_rn], 'Low Temperature': [lo], 'High Temperature': [hi], 'Precipitation': [precipitation],
                            'Humidity': [relative_humidity], 'Pressure': [pressure], 'Wind (strength, direction)': [wind]})


weather_data = weather_data.append(weather_data2)
weather_data.to_excel('./weather-data.xlsx', index=False)

if txt_notifs:
    from twilio.rest import Client





    client = Client(account_sid, auth_token)                    # Twilio Client
    client.messages.create(to=my_number,from_=twilio_number,body=txt_2_me)
