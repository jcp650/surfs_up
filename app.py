# dependencies
from flask import Flask

# Set up flask
app = Flask(__name__)

# Create flask route
@app.route('/')
def hello_world():
    return 'Hello World'

# Skill drill route creation
@app.route('/Tim&Eric/')
def great_job():
    return 'Great Job'