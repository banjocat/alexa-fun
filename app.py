import logging

from flask import Flask
from flask_ask import Ask, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    welcome_message = "Hello. Walter is a baby. He is a beautiful baby that we love. Is Walter the best baby?"
    return question(welcome_message)

@ask.intent('HelloIntent')
def hello():
    greeting = 'Hello Walter'
    return statement(greeting)

@ask.intent('NoIntent')
def no_intent():
    what = 'No. You are wrong. Why would you say such a thing. Walter is the best baby!'
    return statement(what)

@ask.intent('YesIntent')
def yes_intent():
    yes = 'Yes. You are correct. Walter is the best baby.'
    return statement(yes)


if __name__ == '__main__':
    app.run(debug=True)
