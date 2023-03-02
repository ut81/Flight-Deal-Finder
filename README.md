# Flight-Deal-Finder

# APIs Required

1. Google Sheet Data Management - https://sheety.co/
	
2. Kiwi Partners Flight Search API -  https://partners.kiwi.com/

3. Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
	
# Steps to run
1. Go to the link for the [starting Google Sheet and make your own copy of it](https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit?usp=sharing).
2. [ Log into Sheety](https://sheety.co/) with your Google Account (the same account that owns the Google Sheet you copied in step 1).

Make sure you give Sheety permission to access your Google sheets. If you miss this step, log out of Sheety and log in again.

![image](https://user-images.githubusercontent.com/126648429/222382456-82ea93d9-c1b5-4b19-a5cb-8216fb6fa049.png)

Click on "New Project" and create a new project in Sheety with the name "Flight Deals" and paste in the URL of your own Google Sheet.  

Also, enable the POST method in the users endpoint:

![image](https://user-images.githubusercontent.com/126648429/222394068-e33f8d60-9467-48a8-be24-aefcd0586462.png)


7. Copy the sheety price endpoint and paste it into data_manager.py
8. Register with the Kiwi Partners Flight Search API
