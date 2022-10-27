# Control your electrical loads using Google Cloud Platform (GCP)
This is a cloud based control solution for Finnish residents who would like to reduce their electricity bill

## Intro
This simple Python project is evolution from electricity-saver-I project. In this project, we are not using any local computers to run the script thus deploying our code directly into Google Cloud Platform (GCP). Shelly relay is controlled via (Google) cloud - (Shelly) cloud connection. In this project we are requesting electricity prices via this new [API]( https://api.spot-hinta.fi/swagger/ui/#/Pörssihinnat%20tänään%20-%20hinta%20ja%20kuluvan%20tunnin%20'rank'/JustNow) (prices only for Finland, sorry..) which makes the script simpler because we do not need to work with raw data or API key as in "electricity-saver-I" project. 

This project requires no prior knowledge about programming but a curios mind.

## Let's get started
In this demo, we are using [Shelly pro 4PM](https://www.shelly.cloud/knowledge-base/devices/shelly-pro-4pm/) and its first relay output (ID = 0). You can select some other Shelly models of course. **Electrical installation belongs to professional so ask your electrician do Shelly installation.** 

1. Connect Shelly to your home network and make comissioning with [Shelly Cloud App](https://www.shelly.cloud/support/cloud-connected/)
2. Open the app (web or mobile) and find your device ID number (device --> settings --> device ID)
3. Activate authorization for cloud key, copy it as well as server name. You'll need these information in the next step


## spot_shelly.py file modifications


## deploy to Google Cloud Platform (GCP)
Check this tutorial how to activate GCP environment. You should receive 300$ for 90 days and this script is using maybe 5$/month when selecting lowest possible virtual machine. As soon as your Linux Debian machine is up and running look this tutorial how to automate script using "Crontab". Crontab enables script automatization and logging and here are examples about syntax with different time intervals. The spot price is changed every hour 

## Summary
