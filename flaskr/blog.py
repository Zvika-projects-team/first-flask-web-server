from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import time
import random

bp = Blueprint('blog', __name__)

Pool = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
secretPassword = "Hi2U"

delay = 3
delay_next = False

# next_delay = 0.3


@bp.route('/')
def main():
    return render_template('blog/index.html')


@bp.route('/<string:password>/', methods=('GET', 'POST'))
def auth(password=''):
    if (verify_password(password)):
        print("==========good job============")
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

    return delay_basic(paddedInPassword, paddedSecretPassword)

    # return delay_basic(paddedInPassword,paddedSecretPassword)


def delay_basic(paddedInPassword, paddedSecretPassword):
    global delay, delay_next, found
    found = False
    result = True
    count_mistakes = 0
    for i in range(len(paddedSecretPassword)):
        # print("index - " + str(i))
        # print(f"{paddedInPassword[i]} != {paddedSecretPassword[i]}")

        padded_in_char = paddedInPassword[i]
        secret_char = paddedSecretPassword[i]
        input_char = check_num_of_pool_chars(paddedInPassword)
        elegant_statement = ((input_char - 1) % 2 == 0 and ((input_char - 1) / 2) % 2 == 0) or (
                (input_char - 2) % 2 == 0 and ((input_char - 2) / 2) % 2 == 0)

        if paddedInPassword[i] != paddedSecretPassword[i]:
            # underscore code
            if input_char == 0:
                if delay_next:
                    time.sleep(delay)
                    print("-*-*-*-*-*-*-*-*-*-made it-*-*-*-*-*-*-*-*-*-*-")
                    delay_next = False
                    found = True

                if (count_mistakes > len(secretPassword)) and not found:
                    delay_next = True

                count_mistakes += 1
                print(f"mistakes - {count_mistakes}")

            else:
                if input_char != 0:
                    if not elegant_statement:
                        time.sleep(delay)
                    # print(f"=========Incorrect letter=========")

            result = False
            # print(f"=========Incorrect letter=========")

        else:
            if input_char > 0:
                if elegant_statement:
                    time.sleep(delay)
                # print("=========Correct letter=========")
    return result


def check_num_of_pool_chars(password):
    input_char = 0
    for char in password:
        if char in Pool:
            input_char += 1
    return input_char
