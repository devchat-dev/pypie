# -*- coding: utf-8 -*-
""" 
This app is a Slack bot python interpreter. The challenge is to hack it
with only one line of python code.
It also accepts "thx" as feedback and keeps a record of how many it got
in a Firebase DB
"""
from flask import Flask, request
import json
import sys
import os
from io import StringIO
from firebase import firebase


app = Flask(__name__)

# Firebbase configs (for storing thxs)
FIREBASE_URL = os.environ.get("FB_URL")
FIREBASE_TOKEN = os.environ.get("FB_TOKEN")
#if you dont wnat to keep ecord of # of 'thx', set this to False
FB = True
# Slack token
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

# initiate firebase
if FB:
    fb = firebase.FirebaseApplication(FIREBASE_URL, authentication=FIREBASE_TOKEN)

@app.route('/')
def hello_world():
    return 'Hey, my name is pypie!'

@app.route('/message', methods=['POST'])
def chat_message():
    raw_msg = request.form.get('text')
    username = request.form.get('user_name'
    if request.form.get('token') == SLACK_TOKEN:
        old_stdout = sys.stdout
        sys.stdout = strstdout = StringIO()
        if 'thx?' in raw_msg and FB:
            print(int(fb.get('/thxs/thxs_pypie', None)) * '🍪')
        elif 'thx' in raw_msg:
            if FB:
                thxnum = fb.get('/thxs/thxs_pypie', None)
                data = {'thxs_pypie': int(thxnum)+1}
                fb.patch('/thxs', data)
            print('u r welcome')
        elif 'hey' in raw_msg:
            print('hello')
        elif 'ustafa' in raw_msg:
            print("Give him a 🍪!")
        elif 'iffnty' in raw_msg:
            print('the horror!')
        else:
            blacklist = ['app', '__', 'flask', 'import', 'wsgi', 'blacklist', 'sys', 'getattr', 'bytearray',
            'globals', 'locals', 'truncate', 'remove', 'eval', 'exec', '.py', 'pypie', 'exit', 'request']
            msg = raw_msg.split('pypie gimme ')[1]
            if not any(word in msg for word in blacklist):
                exec('print (' + msg + ')')
            else:
                print('sorry, no `{0}` for u, {1}'.format(msg, username)
        return json.dumps({'text': strstdout.getvalue().strip('\n')})
