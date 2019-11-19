from room import Room

import requests

from json import dumps, loads
from keys import api_key



class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom

    def travel(self, direction, showRooms = False):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            if (showRooms):
                nextRoom.printRoomDescription(self)
        else:
            print("You cannot move in that direction.")

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

        json_response = loads(response.text)
        self.currentRoom = json_response
        
        # print(response.text)
        # return loads(response.text)

# Uncomment here to test
json_response = post_move('n')
room = Room(json_response)
print(room.room_id, room.exits)

