from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('HelloIntent')
def hello(firstname):
    test = render_template('jack')
    return statement(text).simple_card('jack', text)

if __name__ == '__main__':
    app.run()
