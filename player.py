import requests
from time import sleep
from keys import api_key
from json import loads


class Player:

    def __init__(self, json_response, currentRoom):
        self.name = json_response['name']
        self.cooldown = json_response['cooldown']
        self.items = json_response['inventory']
        self.currentRoom = currentRoom

    def post_move(self, direction):
        
        if direction is None:
            return "YOU MUST PASS A DIRECTION"
        elif direction != 'n' and direction != 'e' and direction != 's' and direction != 'w':
            return "NOT A VALID DIRECTION"
        
        headers = {
            'Authorization': api_key,
            'Content-Type': 'application/json',
        }

        if direction == 'n':
            data = '{"direction":"n"}'
        elif direction == 's':
            data = '{"direction":"s"}'
        elif direction == 'e':
            data = '{"direction":"e"}'
        else:
            data = '{"direction":"w"}'

        response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=data)

        if response.status_code == 200:
            json_response = loads(response.text)
            return json_response
        else:
            return None


    def get_init(self):
        headers = {
            'Authorization': api_key,
            'Content-Type': 'application/json',
        }
        response = requests.get('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers)
        print(response.text)
        return loads(response.text)

    def post_take(self, item):
        headers = {
            'Authorization': api_key,
            'Content-Type': 'application/json',
        }

        
        if item == 'small treasure':
            data = '{"name":"small treasure"}'
        elif item == 'tiny treasure':
            data = '{"name":"tiny treasure"}'
        elif item == 'shiny treasure':
            data = '{"name":"shiny treasure"}'

        response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/take/', headers=headers, data=data)
        # print(response.text)
        print(response.status_code)
        return loads(response.text)

    # def post_status(self):
    #     headers = {
    #         'Authorization': api_key,
    #         'Content-Type': 'application/json',
    #     }

    #     response = requests.post('https://lambda-treasure-hunt.herokuapp.com/api/adv/status/', headers=headers)
    #     print(response.text)
    #     return loads(response.text)

        # print(response.text)
        # return loads(response.text)
