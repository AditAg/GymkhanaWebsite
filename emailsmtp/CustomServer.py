import smtpd
import asyncore
#from models import Emailmessage
#from django.contrib.auth.models import User

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))
        print('Message :\n', data)
        #for x in rcpttos:
         #   print("Hello")
         #   print (x)
         #   user=User(username=x)
         #   email=Emailmessage()
        #    email.username=user
         #   print(email.username)
         #   email.From=mailfrom
         #   print(email.From)
         #   email.To=x
         #   print(email.To)
         #   email.subject='Test'
         #   print(email.subject)
         #   email.message=data
         #   print(email.message)
         #   email.save()
        file=open('mails.txt','a')
        for x in rcpttos:

            #file.write(str(x)+':-----Message-----\n'+'Subject-"Test"\nMessage-'+str(data)+'\n')
            string=str(str(x)+"=\n------Message------\nSubject:Test\n"+str(data))
            file.write(string)
        file.close()

        return


server = CustomSMTPServer(('127.0.0.1', 1025), None)

asyncore.loop()
