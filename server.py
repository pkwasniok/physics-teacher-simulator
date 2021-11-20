# TODO Endpoint: Calculate users points
# TODO answer/get: Return answers only from other users

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
    cursor.execute('SELECT users.email FROM users')
    users = cursor.fetchall()

    # Extract emails
    emails = []
    for user in users:
        emails.append(user[0])

    # Check if user with specific email exists and create one if not
    if request.args.get('email') not in emails:
        sql = 'INSERT INTO users (email, username) VALUES (%s, %s)'
        val = (request.args.get('email'), 'PhysicsLover' + str(len(emails)))
        cursor.execute(sql, val)
        mydb.commit()

    # Get all user data from db
    cursor.execute('SELECT users.email, users.username, users.superuser, users.daily_question_answered FROM users WHERE users.email=\"' + request.args.get('email')+'\"')
    user = cursor.fetchall()[0]

    return {"status": "OK", "user": {"email": user[0], "username": user[1], "superuser": (True if user[2] == 1 else False), "daily_question_answered": (True if user[3] == 1 else False)}}


@ api.route('/users', methods=['GET'])          # Return list of all users (UNUSED)
def users():
    mydb = db_connect()
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM users')
    mysql_data = cursor.fetchall()

    response = {"users": []}
    for user_data in mysql_data:
        response['users'].append({"email": user_data[1], "username": user_data[2], "points": user_data[3]})

    return response


@api.route('/user/ranking', methods=['GET'])
def user_ranking():
    # Connect to db
    mydb = db_connect()
    cursor = mydb.cursor()

    # Fetch data from db
    cursor.execute('SELECT users.username, reviews.points FROM users INNER JOIN answers ON users.email=answers.email INNER JOIN reviews ON answers.id=reviews.answer_id')
    user_points = cursor.fetchall()

    # Calculate every user points and get list of all users
    points = {}
    usernames = []
    for user in user_points:
        if not user[0] in points:
            points[user[0]] = 0
            usernames.append(user[0])
        points[user[0]] += user[1]

    # Create response
    final_user_points = []
    for username in usernames:
        final_user_points.append({"username": username, "points": points[username]})
    response = {"status": "OK", "ranking": final_user_points}

    return response


@ api.route('/answer/post', methods=['POST'])   # Add new answer to question (f.ex. after daily question)
def answer_post():
    # Connect to db
    mydb = db_connect()
    cursor = mydb.cursor()

    # Insert new answer to db
    sql = 'INSERT INTO answers (email, question, answer) VALUES (%s, %s, %s)'
    val = (request.json['email'], request.json["question"], request.json['answer'])
    cursor.execute(sql, val)

    # Change user daily question answered status
    sql = 'UPDATE users SET users.daily_question_answered=1 WHERE users.email="' + request.json['email'] + '"'
    cursor.execute(sql)

    # Commit all changes to database
    mydb.commit()

    return {"status": "OK"}


@ api.route('/answer/get', methods=['GET'])        # Return all users answers (for asnwer review feature)
def answers():
    mydb = db_connect()
    cursor = mydb.cursor()

    # Fetch data from database
    cursor.execute('SELECT * FROM answers')
    answers = cursor.fetchall()
    cursor.execute('SELECT answer_id, points from reviews WHERE reviews.email="' + request.args.get('email') + '"')
    reviews = cursor.fetchall()

    # Make dict with
    points = {}
    for review in reviews:
        points[review[0]] = review[1]

    # Create response
    response = {"status": "OK", "answers": []}
    for answer in answers:
        reviewed = False
        for review in reviews:
            if answer[0] == review[0]:
                reviewed = True

        response['answers'].append({"id": answer[0], "email": answer[1], "question": answer[2], "answer": answer[3], "time": answer[4], "reviewed": reviewed, "points": (points[answer[0]] if reviewed else "null")})

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

    # Create response
    question = questions['questions'][daily_questions[0]]
    response = {"status": "OK", "question": question['question'], 'branch': question['branch']}

    # Return response
    return response


if __name__ == '__main__':
    api.run()
