from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import time
import random
bp = Blueprint('blog', __name__)

secretPassword = "Pass"

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


delay  = 0.3
next_delay = 0.3 
def verify_password(inPassword):
    global delay
    longPadding = ' '*6
    paddedInPassword = (longPadding + inPassword)[-(len(longPadding)):]
    paddedSecretPassword = (longPadding + secretPassword)[-(len(longPadding)):]
    print(paddedSecretPassword)
    print(paddedInPassword)
    
    return delay_basic(paddedInPassword,paddedSecretPassword)

    #return delay_basic(paddedInPassword,paddedSecretPassword)

delay = 0.15
next_delay = 0.15
def delay_geometric_seq(paddedInPassword, paddedSecretPassword):
    global delay,next_delay
    result = True
    for i in range(len(paddedSecretPassword)):
            #print("index - " + str(i))
            #print(f"{paddedInPassword[i]} != {paddedSecretPassword[i]}")
            if(paddedInPassword[i] != paddedSecretPassword[i]):
                if result == True:
                    next_delay = delay + 0.1
                result = False
                 
                #TODO: add delay functionality here 
                time.sleep(delay)
                print(f"=========Incorrect letter=========")
            else:
                print("=========Correct letter=========")
    delay = next_delay
    return result


def delay_basic(paddedInPassword, paddedSecretPassword):
    global delay
    result = True

    for i in range(len(paddedSecretPassword)):
            #print("index - " + str(i))
            #print(f"{paddedInPassword[i]} != {paddedSecretPassword[i]}")
            if(paddedInPassword[i] != paddedSecretPassword[i]):
                result = False     
                time.sleep(delay)
                print(f"=========Incorrect letter=========")
            else:
                print("=========Correct letter=========")
    delay = next_delay
    return result
