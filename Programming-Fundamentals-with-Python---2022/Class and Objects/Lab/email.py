# Create class Email. The __init__ method should receive sender, receiver and a content.
# It should also have a default set to False attribute called is_sent. The class should have two additional methods:
# ⦁	send() - sets the is_sent attribute to True
# ⦁	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
# You will receive some information (separated by a single space) until you receive the command "Stop".
# The first element will be the sender, the second one – the receiver, and the third one – the content.
# On the final line, you will be given the indices of the sent emails separated by comma and space ", ".
# Call the send() method for the given indices of emails. For each email, call the get_info() method.

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

data_emails = input()

while not data_emails == "Stop":
    sender, receiver, content = data_emails.split() # разделяме на части всеки имейл
    email = Email(sender, receiver, content) # извикваме класа с който ше работим
    emails.append(email) #добавяме към списъка чрез класа

    data_emails = input()

send_emails_index = [int(x) for x in input().split(", ")]

for index_email in send_emails_index: # spored index ot zadadeniq list
    emails[index_email].send() # za vseki index ot lista izvikvame metod send()

for email in emails:       # za vseki  email vyv spisyka ot emails vzimame izvikvame metod chrez koito  poluchavame informaciq
    print(email.get_info())