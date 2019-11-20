from room import Room
from player import Player
import requests
from time import sleep


from json import dumps, loads
from keys import api_key
from room import Room
from path import Path

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


if __name__ == "__main__":
    # json_player = post_status()
    # sleep(5)
    # room_json = get_init()
    # room = Room(room_json)
    # player = Player(json_player, room)

    # path = Path(player)

    b = Path(None).backtrack(['n', 'n', 'n', 'n', 'n', 'w', 'n', 'e'])
    print(b)
    # path.dfs()
