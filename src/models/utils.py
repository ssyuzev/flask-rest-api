import hashlib
import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def set_password(password, salt=None, salt_len=16):
    if not salt:
        salt = get_random_string(salt_len)
    salted_password = salt + password
    h = hashlib.md5(salted_password.encode())
    password_hash = f"{salt}:{h.hexdigest()}"
    return password_hash


def verify_password(hashed_password, new_password):
    salt = hashed_password.split(":")[0]
    if not salt:
        return False
    new_password_hash = set_password(new_password, salt=salt)
    return hashed_password == new_password_hash
