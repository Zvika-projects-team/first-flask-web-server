from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import time
import random

bp = Blueprint('blog', __name__)

Pool = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
secretPassword = "ZviG"

delay = 1


@bp.route('/')
def main():
    return render_template('blog/index.html')


@bp.route('/<string:password>/', methods=('GET', 'POST'))
def auth(password=''):
    global found, delay_next, prev_password
    if verify_password(password):
        print("==========good job============")
        found = False
        delay_next = False
        prev_password = ""
        return b'1'
    else:
        print("==========yikes==========")
        return b'0'


def verify_password(inPassword):
    global delay
    longPadding = ' ' * 6
    paddedInPassword = (longPadding + inPassword)[-(len(longPadding)):]
    paddedSecretPassword = (longPadding + secretPassword)[-(len(longPadding)):]
    print(paddedSecretPassword)
    print(paddedInPassword)

    return encryption(paddedInPassword, paddedSecretPassword)


def encryption(paddedInPassword, paddedSecretPassword):
    global delay
    result = True
    count_mistakes = 0
    for i in range(len(paddedSecretPassword)):

        input_char = check_num_of_pool_chars(paddedInPassword)
        elegant_statement = ((input_char - 1) % 2 == 0 and ((input_char - 1) / 2) % 2 == 0) or (
                (input_char - 2) % 2 == 0 and ((input_char - 2) / 2) % 2 == 0)

        if paddedInPassword[i] != paddedSecretPassword[i]:

            if input_char == 0:
                if (check_num_of_underscores(paddedInPassword) == len(secretPassword) + 2):
                    time.sleep(delay)
            else:
                if input_char != 0:
                    if not elegant_statement:
                        time.sleep(delay)

            result = False

        else:
            if input_char > 0:
                if elegant_statement:
                    time.sleep(delay)
                # print("=========Correct letter=========")
    prev_password = paddedInPassword
    return result


def check_num_of_pool_chars(password):
    input_char = 0
    for char in password:
        if char in Pool:
            input_char += 1
    return input_char


def check_num_of_underscores(password):
    count = 0
    for char in password:
        if char not in Pool and char != ' ':
            count += 1
    return count





def min_encryption(paddedInPassword, paddedSecretPassword):
    global delay
    result = True
    for i in range(len(paddedSecretPassword)):
        input_char = check_num_of_pool_chars(paddedInPassword)
        if paddedInPassword[i] != paddedSecretPassword[i]:
            if input_char == 0:
                time.sleep(delay)
            else:
                pass
            result = False
            
    return result

