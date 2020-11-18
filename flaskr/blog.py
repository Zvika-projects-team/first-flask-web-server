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
def auth(password=''):
    if(verify_password(password)):
        print("==========good job============")
        return b'1'
    else: 
        print("==========yikes==========")
        return b'0'

def verify_password(inPassword):
    result = True
    longPadding = ' '*7
    paddedInPassword = (longPadding + inPassword)[-(len(longPadding)):]
    paddedSecretPassword = (longPadding + secretPassword)[-(len(longPadding)):]
    print(paddedSecretPassword)
    print(paddedInPassword)

    delay = 0.15
    for i in range(len(paddedSecretPassword)):
        #print("index - " + str(i))
        #print(f"{paddedInPassword[i]} != {paddedSecretPassword[i]}")
        if(paddedInPassword[i] != paddedSecretPassword[i]):
            #TODO: add delay functionality here 
            result = False          
            time.sleep(delay)
            print(f"=========Incorrect letter=========")
        else:
            print("=========Correct letter=========")

    return result
