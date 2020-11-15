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
        return b'1'
    else: 
        print("==========yikes==========")
        return b'0'

@bp.route('/success')
def success():
    return render_template('blog/success.html')

@bp.route('/failiure')
def failiure():
    return render_template('blog/failiure.html')

def verify_password(inPassword):
    result = True
    longPadding = ' '*7
    paddedInPassword = (longPadding + inPassword)[-1:-(len(longPadding)):-1]
    paddedSecretPassword = (longPadding + secretPassword)[-1:-(len(longPadding)):-1]
    print(paddedSecretPassword)
    print(paddedInPassword)

    delay_correct = 2
    delay_wrong = 0.01
    for i in range(len(paddedSecretPassword)):
        print("index - " + str(i))
        print(f"{paddedInPassword[i]} != {paddedSecretPassword[i]}")
        if(paddedInPassword[i] != paddedSecretPassword[i]):
            #TODO: add delay functionality here 
            result = False          
            time.sleep(delay_wrong)
            print(f"=========Incorrect letter=========")
        else:
            time.sleep(delay_correct)
            print("=========Correct letter=========")

    return result
