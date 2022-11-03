# The aim of this Python project is to run Shelly relay via Google cloud platform based on 
# hourly spot-price in Finland. All prices are requested through this API: 
# https://api.spot-hinta.fi/swagger/ui/#/Pörssihinnat%20tänään%20-%20hinta%20ja%20kuluvan%20tunnin%20'rank'/JustNow

from urllib import response
import requests
import json
from datetime import datetime

#Type your own Shelly device/system parameters here:
DEVICE_ID = "1234567abcef"
CLOUD_KEY = "1234567890abcdefghijklmn..."
SERVER = "https://shelly-..............."

def main():

    my_limit_price = 0.20  # your own €/kWh price limit (including taxes)

    # get current price from api.spot-hinta.fi
    response_api = requests.get("https://api.spot-hinta.fi/JustNow")
    price_now = response_api.json()
    price_now_with_taxes = float(price_now['PriceWithTax'])

    #Shelly controls via Cloud
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    output = "0"    # This relay is controlled (e.g. Shelly pro 4PM has four relays with output ID's 0,1,2,3. 0 = relay 1, 3 = relay 4 ) 
    
    if price_now_with_taxes <= my_limit_price:
        control = f"id={DEVICE_ID}&auth_key={CLOUD_KEY}&channel={output}&turn=on"
        status = "on"
    else:
        control = f"id={DEVICE_ID}&auth_key={CLOUD_KEY}&channel={output}&turn=off"
        status = "off"

    send_to_shelly = requests.post(f"{SERVER}/device/relay/control", control, headers=headers)
    
    # Date & time
    date = datetime.today().strftime('%d-%m-%Y')
    time = datetime.today().strftime('%H:%M')

    # Getting device status and information for future use (history.txt file)
    data = f"id={DEVICE_ID}&auth_key={CLOUD_KEY}"
    response= requests.post(f"{SERVER}/device/status", data, headers=headers)
    device_status = response.json()
    device_online = device_status["data"]["online"]
    relay_status = device_status["data"]["device_status"][f"switch:{output}"]["output"]
    device_id = device_status["data"]["device_status"]["id"]

    print(f"{date},{time},{DEVICE_ID},{device_online},{price_now_with_taxes},{my_limit_price},{relay_status}")

if __name__ == "__main__":        
    main()
