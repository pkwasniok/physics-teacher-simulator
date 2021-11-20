import mysql.connector
import json

# Load config file
config = json.load(open("./config.json", encoding="utf-8"))

# Connect to mysql
db = mysql.connector.connect(
    host=config['database']['host'],
    user=config['database']['user'],
    password=config['database']['password'],
)
cursor = db.cursor()

# Create database
cursor.execute('CREATE DATABASE ' + config['database']['database'])

# Connect to specific database
db = mysql.connector.connect(
    host=config['database']['host'],
    user=config['database']['user'],
    password=config['database']['password'],
    database=config['database']['database']
)
cursor = db.cursor()

# Create tables in db
cursor.execute('CREATE TABLE answers (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, email VARCHAR(50) NOT NULL, question MEDIUMTEXT NOT NULL, answer LONGTEXT NOT NULL, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)')
cursor.execute('CREATE TABLE users (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, email VARCHAR(50) NOT NULL, username VARCHAR(25) NOT NULL, superuser BOOLEAN DEFAULT FALSE NOT NULL, daily_question_answered BOOLEAN DEFAULT FALSE NOT NULL)')
cursor.execute('CREATE TABLE reviews (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, email VARCHAR(50) NOT NULL, answer_id INT(6) NOT NULL, points INT(3) NOT NULL, comment MEDIUMTEXT NOT NULL)')
