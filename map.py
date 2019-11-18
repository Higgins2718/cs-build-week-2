class Room:
    def __init__(self, name, description, id=0, x=None, y=None):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.getExitsString()}\n"
    def printRoomDescription(self, player):
        print(str(self))
    def getExits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits
    def getExitsString(self):
        return f"Exits: [{', '.join(self.getExits())}]"
    def connectRooms(self, direction, connectingRoom):
        if direction == "n":
            self.n_to = connectingRoom
            connectingRoom.s_to = self
        elif direction == "s":
            self.s_to = connectingRoom
            connectingRoom.n_to = self
        elif direction == "e":
            self.e_to = connectingRoom
            connectingRoom.w_to = self
        elif direction == "w":
            self.w_to = connectingRoom
            connectingRoom.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None
    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
    def getCoords(self):
        return [self.x, self.y]

class Path:
    def __init__(self, player):
        self.player = player
        # create adjacency list with room as key and exits array as value 
        self.mapped = dict()
        self.saved_map = dict()

    def dfs(self):
        path = []
        backTrack = []

        # {0: ['n', 's', 'w', 'e']}
        self.mapped[self.player.currentRoom.id] = self.player.currentRoom.getExits()
        
        # graph consisting of 500 rooms
        while len(self.mapped) < 499:
            if self.player.currentRoom.id not in self.mapped:
                currentroomID = self.player.currentRoom.id
                exits = self.player.currentRoom.getExits()
                # not a mapped room add to map
                self.mapped[currentroomID] = exits
                self.mapped[currentroomID].remove(backTrack[-1])
            # when players hits dead end, backtrack and store path
            while not len(self.mapped[self.player.currentRoom.id]):
                back = backTrack.pop()
                path.append(back)

                # perfrom wait operations
                self.player.travel(back)

            # Get next move
            move = self.mapped[self.player.currentRoom.id].pop(0)
            path.append(move)

            # get inverse room for backTrack
            if move == "n":
                backTrack.append("s")
            elif move == "s":
                backTrack.append("n")
            elif move == "e":
                backTrack.append("w")
            elif move == "w":
                backTrack.append("e")
            
            # travel to next room

            # perfrom wait operations
            self.player.travel(move)
        
        # print(self.mapped)
        print(path)
        return path


class Path:
    def __init__(self, player):
        self.player = player
        # create adjacency list with room as key and exits array as value 
        self.mapped = dict()
        self.saved_map = dict()

    def dfs(self):
        path = []
        backTrack = []

        # {0: ['n', 's', 'w', 'e']}
        self.mapped[self.player.currentRoom.id] = self.player.currentRoom.getExits()
        
        # graph consisting of 500 rooms
        while len(self.mapped) < 499:
            if self.player.currentRoom.id not in self.mapped:
                currentroomID = self.player.currentRoom.id
                exits = self.player.currentRoom.getExits()
                # not a mapped room add to map
                self.mapped[currentroomID] = exits
                self.mapped[currentroomID].remove(backTrack[-1])
            # when players hits dead end, backtrack and store path
            while not len(self.mapped[self.player.currentRoom.id]):
                back = backTrack.pop()
                path.append(back)

                # perfrom wait operations
                self.player.travel(back)

            # Get next move
            move = self.mapped[self.player.currentRoom.id].pop(0)
            path.append(move)

            # get inverse room for backTrack
            if move == "n":
                backTrack.append("s")
            elif move == "s":
                backTrack.append("n")
            elif move == "e":
                backTrack.append("w")
            elif move == "w":
                backTrack.append("e")
            
            # travel to next room

            # perfrom wait operations
            self.player.travel(move)
        
        # print(self.mapped)
        print(path)
        return path
