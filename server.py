from flask import Flask
from flask_cors import CORS
import json
import random
import time
import _datetime
import mysql.connector

# Load config file
config = json.load(open('./config.json'))
questions = json.load(open('./questions.json', encoding='utf-8'))

# Initialize flask and cors
api = Flask(__name__)
cors = CORS(api, resources={r"/*": {"origins": "*"}})

# Create connection with mysql
mydb = mysql.connector.connect(
    host=config.database.host,
    user=config.database.user,
    password=config.database.password
)

# Variables
daily_questions = []


@api.route('/', methods=['GET'])
def home():
    # Load questions and config
    questions = json.load(open('./questions.json', encoding='utf-8'))
    config = json.load(open('./config.json', encoding='utf-8'))

    print(mydb)

    # Check if there are any daily questions left
    global daily_questions
    if len(daily_questions) < 1:
        daily_questions = list(range(0, len(questions['questions'])))
        random.shuffle(daily_questions)
        print(daily_questions)

    # Create response
    question = questions['questions'][daily_questions[0]]
    response = {"question": question['question'], 'branch': question['branch']}

    # Return response
    return response


@api.route('/user', methods=['GET'])
def users():
    return 'essa'


if __name__ == '__main__':
    api.run()
