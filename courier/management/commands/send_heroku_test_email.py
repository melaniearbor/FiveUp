from django.core.management.base import BaseCommand
import email
import smtplib

def testemail():
    print("I'm going to make an email.")
    msg_to = "6102032488@vmobl.com"
    msg = email.message_from_string("Ooh! The test worked!")
    msg['From'] = "melanie_crutchfield@hotmail.com"
    msg['To'] = msg_to
    msg['Subject'] = "" #can leave blank

    print("Here comes the sending!")
    s = smtplib.SMTP("smtp.live.com",587)
    s.ehlo()
    s.starttls() 
    s.ehlo()
    s.login('melanie_crutchfield@hotmail.com', 'crutchback') # TODO set up a user with a password that correlates
    print("I'm logged in")
    #to sending email account

    # s.sendmail(sender, recipient phone number, message) 6192032488@vmobl.com
    s.sendmail("melanie_crutchfield@hotmail.com", msg_to, msg.as_string())

    s.quit()

class Command(BaseCommand):
    def handle(self, *args, **options):
        testemail()
