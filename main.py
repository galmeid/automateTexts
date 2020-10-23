from twilio.rest import Client
import schedule
import random

GOOD_NIGHT_QUOTES = ["Good night!", "Hope you had an amazing day!", "I'm going to sleep now, talk tomorrow?",
                     "Love you! Gn", "Text me when you wake up"]


def automate_texts(texts=GOOD_NIGHT_QUOTES):
    twilio_account = "AC1512436533a410a49c5dda4a74c67e42"
    auth_token = "8ef2622a34500bbb8a245e3daa0cfea8"
    client = Client(twilio_account, auth_token)
    text = texts[random.randint(0, len(texts))]
    client.messages.create(to=str(7657753709), from_=str(3145396409), body=text)

schedule.every().day.at("22:30").do(automate_texts, GOOD_NIGHT_QUOTES)
