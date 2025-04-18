import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):

    chars = set(string.ascii_lowercase)

    if use_uppercase:
        chars.update(string.ascii_uppercase)
    if use_numbers:
        chars.update(string.digits)
    if use_special:
        chars.update(string.punctuation)

    char_list = list(chars)

    password = []

    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    password.append(random.choice(string.ascii_lowercase))

    for _ in range(length - len(password)):
        password.append(random.choice(char_list))

    password_list = list(password)

    random.shuffle(password_list)

    return ''.join(password_list)
