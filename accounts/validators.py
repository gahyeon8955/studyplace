import string
from django.core.exceptions import ValidationError

def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False

def contains_letters(value):
    for char in value:
        if char in string.ascii_letters:
            return True
    return False

def contains_number(value):
    for char in value:
        if char in string.digits:
            return True
    return False

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
            len(password) < 6 or
            not contains_special_character(password) or
            not contains_letters(password) or
            not contains_number(password)
        ):
            raise ValidationError("5~11자의 영문, 숫자, 특수문자 조합이어야 합니다.")
