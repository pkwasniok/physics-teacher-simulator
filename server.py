from flask import Flask
from flask_cors import CORS
import json
import random
import time
import _datetime

# Load config file
config = json.load(open('./config.json'))
questions = json.load(open('./questions.json', encoding='utf-8'))

# Initialize flask and cors
api = Flask(__name__)
cors = CORS(api, resources={r"/*": {"origins": "*"}})


@api.route('/', methods=['GET'])
def home():
    # Load questions and config
    questions = json.load(open('./questions.json', encoding='utf-8'))
    config = json.load(open('./config.json', encoding='utf-8'))

    # Create response
    question = questions['questions'][random.randint(0, len(questions['questions'])-1)]
    response = {"question": question['question'], 'branch': question['branch']}

    # Return response
    return response


if __name__ == '__main__':
    api.run()
