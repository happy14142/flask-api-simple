import json, random
from flask import Flask

name=['dan','bob','susan','kyle','lisa','mary','jack']
employer=['numerix','some boring company']
country=['ireland','texas','the north pole','uk','ny','ni','ontario','alaska']

app = Flask(__name__)

@app.route('/')
def index(): return json.dumps(
    {
        'name': random.choice(name),
        'employer': random.choice(employer),
        'country': random.choice(country)
    })

app.run()
