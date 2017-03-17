from twilio.rest import TwilioRestClient
from key import account_sid, auth_token, my_cell, my_twilio

client = TwilioRestClient(account_sid,auth_token)

my_msg="This is a Text Msg"

message=client.messages.create(to=my_cell,from_=my_twilio,body=my_msg)