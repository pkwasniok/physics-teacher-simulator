import mysql.connector
import json

# Variables
db_name = 'physics_teacher_simulator'

# Load config file
config = json.load(open("./config.json", encoding="utf-8"))

# Connect to mysql
db = mysql.connector.connect(
    host=config['database']['host'],
    user=config['database']['user'],
    password=config['database']['password']
)
cursor = db.cursor()

# Create database
cursor.execute('CREATE DATABASE ' + db_name)

# Connect to specific database
db = mysql.connector.connect(
    host=config['database']['host'],
    user=config['database']['user'],
    password=config['database']['password'],
    database=db_name
)
cursor = db.cursor()

# Create tables in db
cursor.execute('CREATE TABLE answers (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, question VARCHAR(300) NOT NULL, answer VARCHAR(600) NOT NULL, user VARCHAR(60) NOT NULL)')
cursor.execute('CREATE TABLE users (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, username VARCHAR(60) NOT NULL, email VARCHAR(60) NOT NULL, points INT(12) NOT NULL)')
