from flask import *
import json, time


app = Flask(__name__)

@app.routea('/', methods=['GET'])
def home_page():
    data_set ={'Page': 'Home', 'Message': 'Sucessfully loaded the Home page', 'Timestamp': time.time()}
    json_dump = jason.dumps(data_set)

    return json_
