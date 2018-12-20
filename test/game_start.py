import json

user_list = "user.json"
info = ''

try:
    with open(user_list,):
        _user_list = user_list
except FileNotFoundError:
    _user_list = ''
else:
