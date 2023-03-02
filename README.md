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
	
3.  Create a new Sheet (Tab) in your Copy of Flight Deals Google Sheet:
![image](https://user-images.githubusercontent.com/126648429/222386641-fc155e45-36ec-4f58-9097-9e5b0884a09f.png)

4. Add 3 new column headings - "First Name", "Last Name", "Email" to this new user Sheet:
![image](https://user-images.githubusercontent.com/126648429/222386872-53de69b5-a7f4-4bba-9c0a-4688d5d2d045.png)

5. Sync the new sheet in Sheety. you'll need to re-check the PUT checkbox in the prices endpoint.
![image](https://user-images.githubusercontent.com/126648429/222387555-1a370b48-d763-470b-9b5f-0e54c6580159.png)
![image](https://user-images.githubusercontent.com/126648429/222387757-73db374c-f8b2-4496-91eb-9244de36d4d1.png)

6. Now, add First Name,Last Name and Email in User sheet.
7. Copy the sheety price endpoint , and user endpoint and paste it into data_manager.py
8. Register with the Kiwi Partners Flight Search API
