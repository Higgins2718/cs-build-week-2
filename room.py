class Room:
    def __init__(self, json_response):
        self.room_id = json_response['room_id']
        self.name = json_response['title']
        self.cooldown = json_response['cooldown']
        self.terrain = json_response['terrain']
        self.description = json_response['description']
        self.exits = json_response['exits']
        self.items = json_response['items']
        self.errors = json_response['errors']
        self.messages = json_response['messages']
        self.coordinates = json_response['coordinates']

#{'room_id': 19, 'title': 'A misty room', 'description': 'You are standing on grass and surrounded by a dense mist. You can barely make out the exits in any direction.', 'coordinates': '(60,62)', 'elevation': 0, 'terrain': 'NORMAL', 'players': ['player455'], 'items': [], 'exits': ['n', 's', 'w'], 'cooldown': 15.0, 'errors': [], 'messages': ['You have walked south.']}

    # def __str__(self):
    #     return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.getExitsString()}\n"

    # def printRoomDescription(self, player):
    #     print(str(self))

    # def getExits(self):
    #     exits = []
    #     if self.n_to is not None:
    #         exits.append("n")
    #     if self.s_to is not None:
    #         exits.append("s")
    #     if self.w_to is not None:
    #         exits.append("w")
    #     if self.e_to is not None:
    #         exits.append("e")
    #     return exits

    # def getExitsString(self):
    #     return f"Exits: [{', '.join(self.getExits())}]"

    # def connectRooms(self, direction, connectingRoom):
    #     if direction == "n":
    #         self.n_to = connectingRoom
    #         connectingRoom.s_to = self
    #     elif direction == "s":
    #         self.s_to = connectingRoom
    #         connectingRoom.n_to = self
    #     elif direction == "e":
    #         self.e_to = connectingRoom
    #         connectingRoom.w_to = self
    #     elif direction == "w":
    #         self.w_to = connectingRoom
    #         connectingRoom.e_to = self
    #     else:
    #         print("INVALID ROOM CONNECTION")
    #         return None
    # def getRoomInDirection(self, direction):
    #     if direction == "n":
    #         return self.n_to
    #     elif direction == "s":
    #         return self.s_to
    #     elif direction == "e":
    #         return self.e_to
    #     elif direction == "w":
    #         return self.w_to
    #     else:
    #         return None

    # def getCoords(self):
    #     return [self.x, self.y]
