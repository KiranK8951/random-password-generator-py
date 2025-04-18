import string

def validate_yes_no(prompt):
    while True:
        preference = input(prompt).strip().lower()
        if preference in ['yes', 'y']:
            return True
        elif preference in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no' (or 'y'/'n' for short).")

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (8-32 characters): "))
            if 8 <= length <= 32:
                return length
            else:
                print("Password length must be between 8 and 32 characters.")
        except ValueError:
            print("Please enter a valid number.")

def get_use_special_chars():
    return validate_yes_no("Include special characters? (yes/no): ")

def get_use_numbers():
    return validate_yes_no("Include numbers? (yes/no): ")

def get_use_uppercase():
    return validate_yes_no("Include uppercase letters? (yes/no): ")


def get_character_sets():

    # Lowercase letters a-z
    lowercase = string.ascii_lowercase

    # Uppercase letters A-Z
    uppercase = string.ascii_uppercase

    # Digits 0-9
    digits = string.digits

    # Special characters
    special_chars = string.punctuation
    return {
        'lowercase': lowercase,
        'uppercase': uppercase,
        'digits': digits,
        'special': special_chars
    }
