import requests
from json import dumps
from keys import api_key


'''
When calling the below function, refer to this example:
post_move("n")
'''


def post_move(direction):
    if direction is None:
        return "YOU MUST PASS A DIRECTION"
    elif direction != 'n' and direction != 'e' and direction != 's' and direction != 'w':
        return "NOT A VALID DIRECTION"
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json',
    }

    data = '{"direction": "direction_var"}'.replace("direction_var", direction)
    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=data)
    print(response.text)
    return response

def post_take():
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json',
    }

    data = '{"name":"treasure"}'

    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/take/', headers=headers, data=data)
    print(response.text)
    return response

def post_status():
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json',
    }

    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/status/', headers=headers)
    print(response.text)
    return response


'''
When calling the below function, refer to this example:
post_dash("n", "5", "10,19,20,63,72")
'''


def post_dash(direction, num_rooms, next_room_ids):
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json',
    }

    string1 = '{"direction":"direction_var", "num_rooms":"room_var", ' \
           '"next_room_var":"10,19,20,63,72"}'.\
        replace("direction_var", direction)
    string2 = string1.replace("room_var", num_rooms)

    data = string2.replace("next_room_var", next_room_ids)

    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/dash/',
                             headers=headers, data=data)
    print(response.text)
    return response
# Uncomment here to test
# post_move('w')
# post_take()
# post_status()
# post_dash("e", "1", "4")

