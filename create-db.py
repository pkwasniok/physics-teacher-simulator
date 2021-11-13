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
cursor.execute('CREATE TABLE answers (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, question VARCHAR(300) NOT NULL, answer LONGTEXT NOT NULL, time DATETIME NOT NULL, email VARCHAR(60) NOT NULL)')
cursor.execute('CREATE TABLE users (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, email VARCHAR(60) NOT NULL, username VARCHAR(60) NOT NULL, points INT(12) NOT NULL)')
