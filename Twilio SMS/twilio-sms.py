import logging
import json

def sendgrid_email(recepient,message):
    if recepient & message:
        //do nothing
    else:
        logging.info('Check twilio sms arguments')
    value = {
      "body": message,
      "to": recepient
    }
    twilioMessage.set(json.dumps(value))
