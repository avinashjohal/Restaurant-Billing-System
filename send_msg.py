from tkinter import filedialog, messagebox
from twilio.rest import Client
account_SID = 'ACe6a977462be390261d7a2445d910ecec'
auth_Token = '144f9884b49a17f4563afabcfc305b23'

client = Client(account_SID, auth_Token)

message = client.messages.create(
    body=" Hi Avinash Johal.",
    from_='+15094368131',
    to="+918950615338"

)
print(message.sid)

messagebox.showinfo('Send Successfully', 'Message sent succesfully')
