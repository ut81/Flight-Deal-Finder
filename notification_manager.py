import smtplib

my_email="YOUR EMAIL"
passs="YOUR PASSWORD"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_emails(self,message,google_flight_link):
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email,passs)
            
            connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8'))
            
