from twilio.rest import Client
import schedule
import random

GOOD_NIGHT_QUOTES = ["Good night!", "Hope you had an amazing day!", "I'm going to sleep now, talk tomorrow?",
                     "Love you! Gn", "Text me when you wake up"]


def automate_texts(texts=GOOD_NIGHT_QUOTES):
    twilio_account = #Your twilio account
    auth_token = # Your twilio authentication token
    client = Client(twilio_account, auth_token)
    text = texts[random.randint(0, len(texts))]
    client.messages.create(to=str(#phone number to send message to), from_=str(your phone number), body=text)

schedule.every().day.at("22:30").do(automate_texts, GOOD_NIGHT_QUOTES)
