# Control your electrical loads using Google Cloud Platform (GCP), Shelly relay and hourly electricity price (Finland)
This is a cloud based load control solution for Finnish residents (with a spot-price contract) who would like to reduce their electricity bill

## Intro
This simple Python project is an evolution from electricity-saver-I project. In this project, we are not using any local computers to run scripts thus deploying our code directly in Google Cloud Platform (GCP). Our Shelly relay is controlled via (Google) cloud - (Shelly) cloud connection and  we are requesting electricity prices via this new [API]( https://api.spot-hinta.fi/swagger/ui/#/Pörssihinnat%20tänään%20-%20hinta%20ja%20kuluvan%20tunnin%20'rank'/JustNow) (prices only for Finland, sorry..). This makes script simpler because we do not need to work with raw data or with ENTSO-E API key as in "electricity-saver-I" project.

<img src="/images/architecture.jpeg" width="600">

This project requires beginner level knowledge of programming & Linux environments and is meant for people who are intrested smart homes and maybe using already Shelly relays in their home.

## Let's get started
In this demo, we are using [Shelly pro 4PM](https://www.shelly.cloud/knowledge-base/devices/shelly-pro-4pm/) and its first relay output (ID = 0). You can select your own prefered Shelly relay model and expand the script for different or multiply outputs of course. **Note that this kind of electrical installation must be carried out by a professional (= electrician) in Finland so ask your local electrician to do your Shelly installation/wiring.** 

1. connect Shelly to your home network and make basic comissioning with [Shelly Cloud App](https://www.shelly.cloud/support/cloud-connected/)
2. open the app (web or mobile) and copy your relay "DEVICE ID" (Click the device --> Settings --> Device Information --> DEVICE ID).
3. activate the cloud key (User Settings --> Authorization Cloud Key)
<img src="/images/getcloudkey.png" width="600">
4. copy your cloud key and your server name (under the key string). You'll need this information in the next step

## Deploying script to Google Cloud Platform (GCP)
Check [this](https://www.youtube.com/watch?v=lIJlhKrP_SI) tutorial from Algovibes how to run Python in GCP environment. As soon as your Linux Debian virtual machine is installed with Miniconda environment: 

5. open "nano" text editor by typing command line: ```` nano my_spot_script.py ````
6. copy the python script from the repository and paste it to nano editor
7. modify following parameters in the script based on your device: DEVICE_ID, CLOUD_KEY, SERVER
7. close the file by pressing ctrl + x
8. press y (= saving yes) and press enter to save and exit 

Test that your script is working by typing command line: ```` python my_spot_script.py ````

You should see something like this: ````29-10-2022,08:54,*your_device_id*,True,0.0161,0.2,True```` which is a log file we are going to save for the future use. It contains following information: date, UTC time, device ID, Shelly is online (true/false), hour price in kWh with taxes, my limit price in kWh, relay is ON (true/false)?

Great. If you see the output above we are almost there :thumbsup:

### Script automatization with Crontab

[Crontab](https://www.adminschoice.com/crontab-quick-reference) is a file that allows script automatization in Linux environment. This is a great feature in projects like this because we must run the script at least once per hour and check if current electricity price is lower than our limit price. In addition, it also allows to save logs to a text file. Look [this](https://www.youtube.com/watch?v=kjrC1N8K8MI) tutorial from Algovibes how to automate your script using "Crontab". 

If you want to run the script *on the hour* (15:00, 16:00, 17:00 ... and so on) use following syntax:<br>

```` 0 * * * * home/username/miniconda3/bin/python my_spot_script.py >> history.txt ```` 

First five digits/stars * * * * * represents time syntax and more interval examples you'll find from [here](https://crontab.guru/examples.html).

Then comes a path to your Python installation. This you will find by typing: ````which python````. Last but not least, the extension ````>> history.txt```` creates a a file where all outputs: ````29-10-2022,08:54,*your_device_id*,True,0.0161,0.2,True```` are saved. You can open the file later by typing ````nano history.txt```` Note that this file is created after first Crontab run and not before.

## Summary

This project was deployed using GCP. A cloud service comes with a cost but selecting smallest virtual machine available costs should stay under 10 € / month. Google is giving three months free tier (300 $) so testing the system should not generate any costs. Second. Controlling your electrical loads via (two) clouds is exposing your system for cyber attacks comparing local machine running in the local network. If you want to go more secure go for electricity-saver-I approach. Evaluate possible risks in your case and make the call.

That's it. Happy scripting!




