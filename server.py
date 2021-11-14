# TODO Endpoint: Calculate users points

import json
import random
import time
import _datetime
import mysql.connector
from flask import Flask, request
from flask_cors import CORS

# Load config file
config = json.load(open('./config.json'))
questions = json.load(open('./questions.json', encoding='utf-8'))


# Initialize flask and cors
api = Flask(__name__)
cors = CORS(api, resources={r"/*": {"origins": "*"}})


def db_connect():  # Connecting to db
    return mysql.connector.connect(
        host=config['database']['host'],
        user=config['database']['user'],
        password=config['database']['password'],
        database=config['database']['database']
    )


# Variables
daily_questions = []


@api.route('/user/auth', methods=['GET'])       # Authenticate user (after login)
def auth_user():
    mydb = db_connect()
    cursor = mydb.cursor()

    # Check request args
    if request.args.get('email') == None:
        return {"status": "Invaild arguments"}

    # Get users data from db
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    # Extract all emails list
    emails = []
    for user in data:
        emails.append(user[1])

    # Check if user with specific email exists and create one if not
    if request.args.get('email') not in emails:
        sql = 'INSERT INTO users (email, username) VALUES (%s, %s)'
        val = (request.args.get('email'), 'PhysicsLover' + str(len(emails)))
        cursor.execute(sql, val)
        mydb.commit()

    # Get all user data from db
    cursor.execute('SELECT * FROM users WHERE users.email=\"' + request.args.get('email')+'\"')
    user = cursor.fetchall()[0]

    return {"status": "OK", "user": {"email": user[1], "username": user[2], "superuser": (True if user[3] == 1 else False)}}


@ api.route('/users', methods=['GET'])          # Return list of all users (UNUSED)
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


@api.route('/user/ranking', methods=['GET'])
def user_ranking():
    # Connect to db
    mydb = db_connect()
    cursor = mydb.cursor()

    # Fetch data from db
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.execute('SELECT * FROM answers')
    answers = cursor.fetchall()

    usernames = {}
    points = {}
    for user in users:
        usernames[user[1]] = user[2]
        points[usernames[user[1]]] = 0

    print(points)

    for answer in answers:
        points = 0
        for review in json.loads(answer[4])['reviews']:
            print(review)

    return 'OK'


@ api.route('/answer/post', methods=['POST'])   # Add new answer to question (f.ex. after daily question)
def answer():
    # Connect to db
    mydb = db_connect()
    cursor = mydb.cursor()

    # Insert new answer to db
    sql = 'INSERT INTO answers (email, question, answer, reviews) VALUES (%s, %s, %s, %s)'
    val = (request.json['email'], request.json["question"], request.json['answer'], json.dumps({"reviews": []}))
    cursor.execute(sql, val)
    mydb.commit()

    return {"status": "OK"}


@ api.route('/answer/get', methods=['GET'])        # Return all users answers (for asnwer review feature)
def answers():
    mydb = db_connect()
    cursor = mydb.cursor()

    # Fetch data from database
    cursor.execute('SELECT * FROM answers')
    answers = cursor.fetchall()
    cursor.execute('SELECT * from reviews WHERE reviews.email="' + request.args.get('email') + '"')
    reviews = cursor.fetchall()

    # Create response
    response = {"status": "OK", "answers": []}
    for answer in answers:
        reviewed = False
        for review in reviews:
            if answer[0] == review[1]:
                reviewed = True

        response['answers'].append({"id": answer[0], "email": answer[1], "question": answer[2], "answer": answer[3], "time": answer[4], "reviewed": reviewed})

    return response


@api.route('/answer/review/post', methods=['POST'])
def answer_review_post():
    # Connect to db
    mydb = db_connect()
    cursor = mydb.cursor()

    # Check if all arguments are given
    for i in ['answer_id', 'email', 'points', 'comment']:
        if i not in request.json.keys():
            return {"status": "Invaild arguments"}

    print(request.json)
    # Check if answer with specific id exists
    cursor.execute('SELECT id FROM answers WHERE id=' + str(request.json['answer_id']))
    answer = cursor.fetchall()
    if len(answer) != 1:
        return {"status": "Answer not found"}

    # Add review to db
    sql = 'INSERT reviews (answer_id, email, points, comment) VALUES (%s, %s, %s, %s)'
    val = (request.json['answer_id'], request.json['email'], request.json['points'], request.json['comment'])
    cursor.execute(sql, val)
    mydb.commit()

    return {"status": "OK"}


@ api.route('/daily_question', methods=['GET'])  # Return todays daily question
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


if __name__ == '__main__':
    api.run()
