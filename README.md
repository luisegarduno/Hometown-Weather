
     __       __            __       __                        __      __
    /  \     /  |          /  |  _  /  |                      /  |    /  |
    $$  \   /$$ | __    __ $$ | / \ $$ |  ______    ______   _$$ |_   $$ |____    ______    ______
    $$$  \ /$$$ |/  |  /  |$$ |/$  \$$ | /      \  /      \ / $$   |  $$      \  /      \  /      \
    $$$$  /$$$$ |$$ |  $$ |$$ /$$$  $$ |/$$$$$$  | $$$$$$  |$$$$$$/   $$$$$$$  |/$$$$$$  |/$$$$$$  |
    $$ $$ $$/$$ |$$ |  $$ |$$ $$/$$ $$ |$$    $$ | /    $$ |  $$ | __ $$ |  $$ |$$    $$ |$$ |  $$/ 
    $$ |$$$/ $$ |$$ \__$$ |$$$$/  $$$$ |$$$$$$$$/ /$$$$$$$ |  $$ |/  |$$ |  $$ |$$$$$$$$/ $$ |
    $$ | $/  $$ |$$    $$ |$$$/    $$$ |$$       |$$    $$ |  $$  $$/ $$ |  $$ |$$       |$$ |
    $$/      $$/  $$$$$$$ |$$/      $$/  $$$$$$$/  $$$$$$$/    $$$$/  $$/   $$/  $$$$$$$/ $$/
                 /  \__$$ |
                 $$    $$/                
                  $$$$$$/                 ~ Website : https://garduno.me


# MyWeather   

MyWeather is a python script that uses the AccuWeather API to retrieve weather data given a specific zip code.     

Features:     
- Collected data is written to an Excel file     
- Forward daily data to personal phone number using Twilio (see below)

### Prerequisites:    
- Python (>= 3.5) 
    - [Windows Installer](https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe)
    - [MacOS Installer](https://www.python.org/ftp/python/3.9.2/python-3.9.2-macosx10.9.pkg)
- Have the following python modules installed: xlrd, lxml, pandas, urllib3, requests, openpyxl, xlsxwriter     
  - If you don't have them installed the script will install them for you!
- AccuWeather Developer account (easy)     
  1. Visit the [AccuWeather Developer](https://developer.accuweather.com/user/register) portal, & enter necessary information.
  2. Activate your profile using the confirmation link sent to the email address you provided.
  3. Visit the ['My Apps'](https://developer.accuweather.com/user/me/apps) tab & click on '+ Add a new App'
  4. Give the app a name, and under 'What will you be creating with this API?' select 'Weather App'. Then click 'Create App'
  5. Now click the newly created [App](https://developer.accuweather.com/user/me/apps#my-apps-collapse0) to reveal the API Key 

## Option 1 : Without text-messages

### Instructions (without Twilio)
1.) Deploy! - Paste this in your terminal (`python [MyWeather.py](https://github.com/luisegarduno/MyWeather/releases/download/1.0/MyWeather.py)`)     
2.) Insert your AccuWeather API Key when prompted to

## Option 2 : With text-messages
### Prerequisites:
- Have the twilio python modules installed     
  - If you don't have twilio installed the script will install it for you      
- Valid (personal/work) phone number
- Twilio account + Twilio phone number (see instructions below).
  - Skip to step #4 of instructions if you already have both of these.

### Instructions w/ Twilio:
1.) [Sign up](https://www.twilio.com/try-twilio) or [log in](https://www.twilio.com/login) to Twilio.    
2.) After account has been confirmed via email, visit your [console](https://www.twilio.com/console) to find your API crendentials (under `project info`).    
3.) Obtain a phone number via Twilio (2 methods):      
- Method 1: [Trial](https://www.twilio.com/console/phone-numbers/trial-number/modal?capability[]=sms)    
- Method 2: [Purchase](https://www.twilio.com/console/phone-numbers/search)     
4.) Deploy! - Paste this in your terminal (`python [MyWeather.py](https://github.com/luisegarduno/MyWeather/releases/download/1.0/MyWeather.py)`)      
5.) Insert your AccuWeather API key +  Twilio crendentials + Phone Numbers when prompted to
