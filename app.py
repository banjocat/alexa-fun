import logging

from flask import Flask
from flask_ask import Ask, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

REPROMPT_TEXT = 'Sorry, I did not understand you. The correct answer is Yes. Please try again. Is Walter the best baby?'

@ask.launch
def launch():
    welcome_message = "Hello Muratore family. Walter is a baby. He is a beautiful baby that we love. Is Walter the best baby?"
    return question(welcome_message).reprompt(REPROMPT_TEXT)

@ask.intent('HelloIntent')
def hello():
    greeting = 'Saying Hello to Walter is nice. But I asked a question. Is Walter the best baby?'
    return question(greeting).reprompt(REPROMPT_TEXT)

@ask.intent('MeowIntent')
def cats():
    meow = 'Cats is not an answer. It is true that you have two cats named Monster and Ollie, but I asked if Walter is the best baby. Please answer!'
    return question(meow).reprompt(REPROMPT_TEXT)

@ask.intent('NoIntent')
def no_intent():
    what = 'No. You are wrong. Why would you say such a thing. Walter is the best baby! Please try again and say the correct answer!'
    return question(what).reprompt(REPROMPT_TEXT)

@ask.intent('YesIntent')
def yes_intent():
    yes = 'Yes. You are correct. Walter is the best baby. Walter. Please go give Momma a hug now.'
    return statement(yes)


if __name__ == '__main__':
    app.run(debug=True)
