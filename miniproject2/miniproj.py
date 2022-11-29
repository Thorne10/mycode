#!/usr/bin/env python3
from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import random

app = Flask(__name__)

# FAMILY GUY QUOTES
# two endpoints
# one endpoint shows json
# one endpoint shows a jinja2 html page

quotes= {"Peter Griffin" : ["I have an idea so smart that my head would explode if I even began to know what I was talking about.",
                            "Pea.. tear.. Gryphon. Yeah Peter Griffin! Aw crap.","I got drunk and then got my picture taken, so that way When I get pulled over for drunk drivin' I look the same as on my license."],

         "Chris Griffin" : ["I just want peace on Earth. That's better than being selfish like Meg, right? So I should get more than her.", "I don't have to listen to you, you're a dog, you don't have a soul!"],

         "Stewie Griffin": ["Oh, and tell Cookie Monster not to phone me until he finishes rehab.","What the deuce?",],

         "Brian Griffin" : ["Whose leg do you have to hump to get a dry martini around here?","I'm not drunk! I just have speech impediment... And a stomach virus... And an inner ear infection.",],

         "Quagmire" : ["He's a baby who did a baby thing. Let’s all calm down a little.","What a surprise, the mugger's never heard of Truman Capote.",]}
@app.route("/quotes")
def familyguyquotes():
    return quotes

@app.route("/")
def index():
    random.choice(list(quotes))
    characters = random.choice(list(quotes))
    return render_template("miniproj.html",thecharacter = characters,thequote = random.choice(quotes[characters]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
