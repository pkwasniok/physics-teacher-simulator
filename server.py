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

# questions status
# 0 - idle
# 1 - daily_question
# 2 - used

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


@api.route('/users', methods=['GET'])              # Return list of all users (UNUSED)
def users():
    mydb = db_connect()
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM users')
    mysql_data = cursor.fetchall()

    response = {"users": []}
    for user_data in mysql_data:
        response['users'].append({"email": user_data[1], "username": user_data[2], "points": user_data[3]})

    return response


@api.route('/user/ranking', methods=['GET'])        # Returns ranking
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


@api.route('/user/answers', methods=['GET'])        # Returns list of all answers
def user_answers():
    # Connect to db
    mydb = db_connect()
    cursor = mydb.cursor()

    # Fetch data
    cursor.execute('SELECT answers.id, answers.question, answers.answer, answers.time, reviews.points, reviews.comment FROM answers LEFT JOIN reviews ON answers.id=reviews.answer_id WHERE answers.email="' + request.args['email'] + '"')
    answers = cursor.fetchall() 

    # Create response
    response = {"status": "OK", "answers": []}
    answers_in_response = []
    for answer in answers:
        if not answer[0] in answers_in_response:
            answers_in_response.append(answer[0])
            answer_dict = {
                "id": answer[0],
                "question": answer[1],
                "answer": answer[2],
                "time": answer[3],
                "reviews": [{"points": answer[4], "comment": answer[5]}] 
            }
            response['answers'].append(answer_dict)
        else:
            response['answers'][answers_in_response.index(answer[0])]['reviews'].append({"points": answer[4], "comment": answer[5]})

    print(response)

    return response


@api.route('/user/settings/username', methods=['POST'])
def user_settings_username():
    mydb = db_connect()
    cursor = mydb.cursor()

    # Validate post body
    if request.json.get('email') == None or request.json.get('username') == None:
        return {'status': 'Invalid arguments'}

    # Update username in db
    cursor.execute('UPDATE users SET username=%s WHERE users.email=%s', (request.json.get('username'), request.json.get('email')))
    mydb.commit()

    return {'status': 'OK'}


@api.route('/answer/post', methods=['POST'])       # Add new answer to question (f.ex. after daily question)
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


@api.route('/answer/get', methods=['GET'])        # Return all users answers (for asnwer review feature)
def answers():
    mydb = db_connect()
    cursor = mydb.cursor()

    # Fetch data from database
    cursor.execute('SELECT * FROM answers WHERE NOT email="' + request.args.get('email') + '"')
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


@api.route('/answer/review/post', methods=['POST'])# Post answer review
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


@ api.route('/daily_question', methods=['GET'])     # Return todays daily question
def daily_question():
    mydb = db_connect()    
    cursor = mydb.cursor()

    # Read daily questions queue
    questions_queue = json.load(open('./questions.json'))
    confgi = json.load(open('./config.json'))

    # Take new question when time is ok xD
    now = _datetime.datetime.now()
    then = _datetime.datetime.strptime(questions_queue['last_generation'], '%Y-%m-%d')
    generation_hour = _datetime.datetime.strptime(config['daily_question']['generation_hour'], '%H:%M')
    if (now-then).days >= 1 and len(questions_queue['queue']) > 0:
        if now.hour >= generation_hour.hour and now.minute >= generation_hour.minute:
            questions_queue['queue'].pop(0)
            questions_queue['last_generation'] = now.strftime('%Y-%m-%d')
            with open('./questions.json', 'w') as f:
                json.dump(questions_queue, f)

    # Generate new daily questions list if empty
    if len(questions_queue['queue']) <= 0:
        cursor.execute('SELECT id FROM questions')
        questions_id = cursor.fetchall()

        for id in questions_id:
            questions_queue['queue'].append(id[0])

        random.shuffle(questions_queue['queue'])        

        with open('./questions.json', 'w') as f:
            json.dump(questions_queue, f)
           
    # Generate response with daily questions
    cursor.execute('SELECT author_email, question, branch FROM questions WHERE questions.id=' + str(questions_queue['queue'][0]))
    daily_question = cursor.fetchall()[0]
    response = {"status": "OK", "daily_question": {
        "author_email": daily_question[0],
        "question": daily_question[1],
        "branch": daily_question[2]
    }}

    # Return response
    return response


if __name__ == '__main__':
    api.run()
