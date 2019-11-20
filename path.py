from time import sleep
from room import Room


class Path:
    def __init__(self, player):
        self.player = player
        # create adjacency list with room as key and exits array as value
        self.mapped = dict()
        self.saved_map = []


    def backtrack(self, arr):
        backTrack = []
        for move in arr:
            if move == "n":
                backTrack.append("s")
            elif move == "s":
                backTrack.append("n")
            elif move == "e":
                backTrack.append("w")
            elif move == "w":
                backTrack.append("e")
        backTrack.reverse()
        print(backTrack)
        print(f"\n\n{self.player.currentRoom.room_id}: {self.player.currentRoom.name} - {self.player.currentRoom.description} - {self.player.currentRoom.items}\n")
        sleep(15)
        for move in backTrack:
            room = Room(self.player.post_move(move))

            self.player.currentRoom = room
            print(f"\n\n{self.player.currentRoom.room_id}: {self.player.currentRoom.name} - {self.player.currentRoom.description} - {self.player.currentRoom.items}\n")
            sleep(self.player.currentRoom.cooldown)


        

    def dfs(self):
        path = []
        backTrack = []

        # {0: ['n', 's', 'w', 'e']}
        self.mapped[self.player.currentRoom.room_id] = self.player.currentRoom.exits
        # graph consisting of 500 rooms
        sleep(2)
        while len(self.mapped) < 499:

            if self.player.currentRoom == None:
                print("found nil")
                break
            print(f"\n\n{self.player.currentRoom.room_id}: {self.player.currentRoom.name} - {self.player.currentRoom.description} - {self.player.currentRoom.items}\n{path}")
            if self.player.currentRoom.room_id not in self.mapped:
                self.saved_map.append(self.player.currentRoom)
                
                currentroomID = self.player.currentRoom.room_id
                exits = self.player.currentRoom.exits
                # not a mapped room add to map
                self.mapped[currentroomID] = exits
                self.mapped[currentroomID].remove(backTrack[-1])
            # when players hits dead end, backtrack and store path
            while not len(self.mapped[self.player.currentRoom.room_id]):
                back = backTrack.pop()
                path.append(back)

                # perfrom wait operations
                room = Room(self.player.post_move(move))
                self.player.currentRoom = room
                # self.player.currentRoom = Room(json_response)
                # wait = self.player.currentRoom.cooldown
                sleep(15)

            # Get next move
            move = self.mapped[self.player.currentRoom.room_id].pop(0)
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
            room = Room(self.player.post_move(move))
            self.player.currentRoom = room
            # self.player.currentRoom = Room(json_response)
            # wait = self.player.currentRoom.cooldown
            sleep(15)
        # print(self.mapped)
        print(path)
        print(self.saved_map)
        return path
