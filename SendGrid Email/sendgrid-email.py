import logging
import json

def sendgrid_email(Erecepient,Esubject,Ebody):
    if Ebody & Esubject & Ebody:
        //do nothing
    else:
        logging.info('Check sendgrid email arguments')
    message = {
        "personalizations": [ {
          "to": [{
            "email": Erecepient
            }]}],
        "subject": Esubject,
        "content": [{
            "type": "text/plain",
            "value": Ebody }]}
    sendGridMessage.set(json.dumps(message))
