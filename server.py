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


def db_connect():
    return mysql.connector.connect(
        host=config['database']['host'],
        user=config['database']['user'],
        password=config['database']['password'],
        database=config['database']['database']
    )


# Variables
daily_questions = []


@api.route('/daily_question', methods=['GET'])
def daily_question():
    # Load questions and config
    questions = json.load(open('./questions.json', encoding='utf-8'))
    config = json.load(open('./config.json', encoding='utf-8'))

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


@api.route('/users', methods=['GET'])
def users():
    mydb = db_connect()
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM users')
    mysql_data = cursor.fetchall()

    response = {"users": []}
    for user_data in mysql_data:
        response['users'].append({"email": user_data[1], "username": user_data[2], "points": user_data[3]})

    print(response)
    return response


@api.route('/answer', methods=['POST'])
def answer():
    question = request.json['question']
    answer = request.json['answer']
    email = request.json['email']

    mydb = db_connect()
    cursor = mydb.cursor()

    sql = 'INSERT INTO answers (question, answer, email, time) VALUES (%s, %s, %s, %s)'
    val = (question, answer, email, str(_datetime.datetime.now().isoformat()))
    cursor.execute(sql, val)

    mydb.commit()

    return 'OK'


@api.route('/answers', methods=['GET'])
def answers():
    mydb = db_connect()
    cursor = mydb.cursor()

    # Fetch data from database
    cursor.execute('SELECT * FROM answers')
    answers = cursor.fetchall()
    cursor.execute('SELECT * from users')
    users = cursor.fetchall()

    # Get list of all usernames and email
    usernames = {}
    for user in users:
        usernames[user[1]] = user[2]

    # Create response
    response = {"answers": []}
    for answer in answers:
        response['answers'].append({"id": answer[0], "question": answer[1], "answer": answer[2], "username": usernames[answer[4]], "time": answer[3]})

    return response


if __name__ == '__main__':
    api.run()
