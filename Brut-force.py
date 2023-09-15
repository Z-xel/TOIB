import string
import itertools
import time

#условный пароль
password_real = "slav"
start_time = time.time()

guess_password_set = string.digits + string.ascii_letters + string.punctuation
guess_password_length = 1


def string_iter(string, length):
    yield from itertools.product(string, repeat=length)


while True:
    for password_set in string_iter(guess_password_set, guess_password_length):
        password_string = ''.join(password_set)
        if password_string == password_real:
            end_time = time.time()
            exec_time = end_time - start_time
            print("Password is found for {}s: {}"
                  .format(exec_time, password_string))
            exit()
    guess_password_length += 1