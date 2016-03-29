
# # A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

from flask import Flask, request
import json
import sys
from io import StringIO

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask4!'

@app.route('/message', methods=['POST'])
def chat_message():
    old_stdout = sys.stdout
    sys.stdout = strstdout = StringIO()
    if 'thx' in request.form.get('text'):
        print('u r welcome')
    else:

        msg = request.form.get('text').split('pypie gimme ')[1]
        if 'app' not in msg or '__' not in msg or 'flask' not in msg:
            exec('print (' + msg + ')')
    return json.dumps({'text': strstdout.getvalue().strip('\n')})
    #return json.dumps({'text': 'zzzzzz'})
