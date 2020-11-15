from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import time
import random
bp = Blueprint('blog', __name__)

secretPassword = "Hello"


@bp.route('/',methods=('GET', 'POST'))
def index():
    password = "_"*30
    print("========start=========")
    if request.method == 'POST':
        password = request.form['password']
    if( password != '_'*30):
        if(verify_password(password)):
            print("==========good job============")
            return redirect(url_for('blog.success'))
        else: 
            flash("Incorrect password")
            print("==========yikes==========")
    return render_template('blog/index.html')

@bp.route('/success')
def success():
    return render_template('blog/success.html')

def verify_password(inPassword):
    result = True
    longPadding = ' '*30
    paddedInPassword = (longPadding + inPassword)[-1:-(len(longPadding)):-1]
    paddedSecretPassword = (longPadding + secretPassword)[-1:-(len(longPadding)):-1]
    print(paddedSecretPassword)
    print(paddedInPassword)

    delay = 0.7
    for i in range(len(paddedSecretPassword)):
        print("index - " + str(i))
        if(paddedInPassword[i] != paddedSecretPassword[i]):
            #TODO: add delay functionality here 
            result = False          
            time.sleep(delay- random.uniform(0.01,0.2))
            print("=========Incorrect letter=========")
        else:
            time.sleep(delay)
            print("=========Correct letter=========")

    return result
