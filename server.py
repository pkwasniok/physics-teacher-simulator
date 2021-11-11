from flask import Flask, request
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
    host=config['database']['host'],
    user=config['database']['user'],
    password=config['database']['password'],
    database=config['database']['database']
)


def db_connect():
    return mysql.connector.connect(
        host=config['database']['host'],
        user=config['database']['user'],
        password=config['database']['password'],
        database=config['database']['database']
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


@api.route('/answer', methods=['POST'])
def users():
    print(request.json['question'])
    question = request.json['question']
    answer = request.json['answer']
    email = request.json['email']

    mydb = db_connect()
    cursor = mydb.cursor()

    sql = 'INSERT INTO answers (question, answer, email) VALUES (%s, %s, %s)'
    val = (question, answer, email)
    cursor.execute(sql, val)

    mydb.commit()

    return 'OK'


if __name__ == '__main__':
    api.run()
