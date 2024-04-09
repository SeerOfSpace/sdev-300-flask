"""lab6"""
import re
#import logging
#from pathlib import Path
from datetime import datetime

from flask import Flask, render_template, redirect, request

app = Flask(__name__)
#main_path = Path(__file__).parent
#logging.basicConfig(level='DEBUG')

@app.route("/")
def root():
    """redirect root to home"""
    return redirect('/home', code=301)


@app.route('/home')
def home():
    """function for home page"""
    return render_template('home.html.jinja')


@app.route('/datetime')
def datetime_page():
    """function for datetime page"""
    datetime_var = datetime.now()
    return render_template(
        'datetime.html.jinja',
        datetime=datetime_var.strftime(r'%d/%m/%Y, %I:%M:%S %p')
    )


@app.route('/xsstest', methods=['GET'])
def xsstest():
    """function for xsstest page. takes a single query parameter"""
    unsanitized_input = request.args.get('input1') or ''
    matches = re.findall(r'[a-zA-Z0-9 ]+', unsanitized_input)
    sanitized_input = ''.join(matches)
    return render_template('xsstest.html.jinja', input1=sanitized_input, input2=unsanitized_input)
