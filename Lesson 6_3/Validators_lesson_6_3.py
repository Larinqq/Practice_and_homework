import re
import string


def check_pin(pin):
    """
    Checks if pin contains only digits, if digits are different and pin is not '1234'
    :param pin: (str)
    :return: boolean
    """
    if not pin.isdigit():
        return False

    elif len(set(pin)) == 1:
        return False

    elif pin == "1234":
        return False

    return True


def check_pass(password):
    """
    Checks if password is longer than 8 characters and consists of both digits and letters
    :param password: string
    :return: boolean
    """
    if len(password) < 8:
        return False

    has_letters = False
    has_digits = False

    for ch in password:
        if ch in string.ascii_letters:
            has_letters = True
        elif ch in string.digits:
            has_digits = True

    return has_letters and has_digits


def check_mail(mail):
    """
    Checks email
    :param mail: string
    :return: boolean
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pattern, mail) is None:
        return False

    return True


def check_name(name):
    """
    Checks if name consist of only Russian letters and spaces
    :param name:
    :return: boolean
    """
    pattern = r'^[А-Яа-яеЕёЁ\s]+$'
    if re.match(pattern, name):
        return True
    else:
        return False
