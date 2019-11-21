from room import Room
from player import Player
import requests
from time import sleep
from json import dumps, loads
from keys import api_key
from room import Room
from path import Path


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

# Uncomment here to test
def get_init():
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json',
    }
    response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
    # print(response.text)
    return loads(response.text)


def post_status():
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json',
    }

    response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/status/', headers=headers)
    print(response.text)
    return loads(response.text)


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

if __name__ == "__main__":
    json_player = post_status()
    sleep(5)
    room_json = get_init()
    room = Room(room_json)
    player = Player(json_player, None)
    player.currentRoom = room

    path = Path(player)

    # path.backtrack(['s', 's', 's', 's', 's', 'e', 's', 'e', 's', 's', 's', 'e', 's', 's'])
    # l = ['n', 'n', 'n', 'n', 'n', 'w', 'n', 'e', 'w', 'w', 'n', 'n', 'n', 'e', 'w', 'w', 'n', 'n', 'n', 'n', 's', 'e', 'n', 's', 'w', 's', 's', 'e', 'w', 'w', 'n', 'n', 's', 's', 'e', 's', 'e', 's', 'e', 'e', 'w', 'w', 's', 'w', 'n', 's', 'w', 'n', 'n', 's', 'w', 'n', 'n', 'n', 'n', 'n','n', 's', 's', 's', 's', 's', 's', 'e', 'n', 's', 's', 'e', 'n', 's', 'e', 'n', 'n', 'e', 'w', 'w', 'n', 'n', 'n', 'n', 's', 'e', 'n', 's', 'w', 's', 's', 'e', 'w', 'w', 'n', 'n', 's', 's', 'e', 's', 'e', 's', 'e', 'e', 'w', 'w', 's', 's', 'e', 's', 'e', 's', 's', 's', 's', 's', 's', 's', 'w', 'n', 'w', 'n', 'w', 'n', 'n', 's', 'w', 'e', 's', 'w', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 'e', 's', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 'n', 'e', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'e', 'n', 'n', 'e', 'n', 'e', 'n', 'e', 's', 'e', 's', 'e', 'w', 'n', 'e', 'n', 'e', 'e', 's', 'e', 'e', 's', 'n', 'e', 'w', 'w', 'w', 'n', 'e', 'n', 'e', 'e', 'e', 'w', 'w', 'w', 's', 'e', 'w', 'w', 'w', 'w', 's', 'e', 's', 's', 's', 's', 's', 's']
    l = ['n', 'n']
    # path.backtrack(l)
    # print(len(l))
    path.dfs()

