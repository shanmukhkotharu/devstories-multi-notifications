import logging
from azure.communication.sms import SmsClient

def mysms_AZcom(recepient,value):
    # configuring your account.
    connection_string = os.getenv('COMMUNICATION_SERVICES_CONNECTION_STRING')
    # Creating the Client object which is used to send SMS.
    sms_client = SmsClient.from_connection_string(connection_string)
    from_phone="xxxxxxxxxx"
    if to_phone:
        //do nothing
    else:
        logging.info('couldnt get recepient phone number')
    if value:
        //do nothing
    else:
        //asuming it is intentional for testing
        value="You got this!!"
    sms_responses = sms_client.send(
        from_=from_phone,
        to=to_phone,
        message=value,
        enable_delivery_report=True, # optional
        tag="custom-tag") # optional
    if sms_responses:
        logging.info('Requested to send sms to '+to_phone+' with text: '+value)
