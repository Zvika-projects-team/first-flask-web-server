from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import time
import random
bp = Blueprint('blog', __name__)

secretPassword = "Hello"

@bp.route('/')
def main():
    return render_template('blog/index.html')


@bp.route('/<string:password>/',methods=('GET', 'POST'))
def index(password):
    if(verify_password(password)):
        print("==========good job============")
        return redirect(url_for('blog.success'))
    else: 
        print("==========yikes==========")
        return redirect(url_for('blog.failiure'))

@bp.route('/success')
def success():
    return render_template('blog/success.html')

@bp.route('/failiure')
def failiure():
    return render_template('blog/failiure.html')

def verify_password(inPassword):
    result = True
    longPadding = '_'*30
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
