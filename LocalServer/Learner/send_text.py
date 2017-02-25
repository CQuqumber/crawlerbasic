from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "AC92288ddd03494491f81d69958319567e" # Your Account SID from www.twilio.com/console
auth_token  = "d72fb50425172d292d3e242ecc060216"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(
    	body="Hello from Python",
        to="+886921581506",    # Replace with your phone number
        from_="+12058720696") # Replace with your Twilio number
except TwilioRestException as e:
    print(e)