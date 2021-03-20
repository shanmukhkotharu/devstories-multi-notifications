import logging
import json

def twilio_sms(recepient,message):
    if recepient & message:
        //do nothing
    else:
        logging.info('Check twilio sms arguments')
    value = {
      "body": message,
      "to": recepient
    }
    twilioMessage.set(json.dumps(value))
