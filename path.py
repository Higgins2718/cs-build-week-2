from time import sleep
from room import Room

name_changer = 467 #: Pirate Ry's

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
        arr.reverse()
        print(f"\n\n{self.player.currentRoom.room_id}: {self.player.currentRoom.name} - {self.player.currentRoom.description} - {self.player.currentRoom.items}\n")
        sleep(15)
        for move in backTrack:
            room = Room(self.player.post_move(move))
            self.player.currentRoom = room
            print(f"\n\n{self.player.currentRoom.room_id}: {self.player.currentRoom.name} - {self.player.currentRoom.description} - {self.player.currentRoom.items}\n")
            sleep(self.player.currentRoom.cooldown)


    def statusPrint(self, path):
        with open('statusprint.txt', 'a') as statusprintfile:
            statusprintfile.write(f"Current Room ID: {self.player.currentRoom.room_id}\nCurrent Room Name: {self.player.currentRoom.name}\nRoom Coordinates: {self.player.currentRoom.coordinates}\nRoom Items: {self.player.currentRoom.items}\nPath: {path}\n\n")

        print(f"\n\n{self.player.currentRoom.room_id}: {self.player.currentRoom.name} - moves: {self.player.currentRoom.exits}\n{self.player.currentRoom.description}\nerror: {self.player.currentRoom.errors} \n{self.player.currentRoom.items}\n{path}\n")

    def backStatusPrint(self, backTrack):
        print(f"\n\nbackTrack<---{self.player.currentRoom.room_id}: {self.player.currentRoom.name} - moves: {self.player.currentRoom.exits} -{self.player.currentRoom.description} - error: {self.player.currentRoom.errors} - {self.player.currentRoom.items}\n{backTrack}")

    def dfs(self):
        path = []
        backTrack = []

        # {0: ['n', 's', 'w', 'e']}
        self.mapped[self.player.currentRoom.room_id] = self.player.currentRoom.exits
        
        self.saved_map.append(self.player.currentRoom.room_id)
        # graph consisting of 500 rooms
        sleep(5)
        while len(self.mapped) < 499:
            # write this to file 
            self.statusPrint(path)
            # print(f"\n\n{self.player.currentRoom.room_id}: {self.player.currentRoom.name} - moves: {self.player.currentRoom.exits}\n{self.player.currentRoom.description}\nerror: {self.player.currentRoom.errors} \n{self.player.currentRoom.items}\n{path}\nmaped: {self.saved_map}")

            if self.player.currentRoom.room_id == name_changer:
                print('in name changer room')
                break

            if self.player.currentRoom.room_id == 0:
                print('in room 0')
                break

            if self.player.currentRoom.name == 'Shop':
                print('in shop!')
                break
            
            # UNCOMMENT THIS TO PICK UP ALLLL THE TREASURE
            # if len(self.player.currentRoom.items) > 0:
            #     for item in self.player.currentRoom.items:
            #         j = self.player.post_take(item)
            #         sleep(5)
            #         self.player.currentRoom = Room(j)
            #         print(self.player.currentRoom.messages)
            #         sleep(self.player.currentRoom.cooldown)

            if self.player.currentRoom.room_id not in self.mapped:
                self.saved_map.append(self.player.currentRoom)

                currentroomID = self.player.currentRoom.room_id
                exits = self.player.currentRoom.exits
                
                # not a mapped room add to map
                self.mapped[currentroomID] = exits
                self.mapped[currentroomID].remove(backTrack[-1])
            # when players hits dead end, backtrack and store path
            while not len(self.mapped[self.player.currentRoom.room_id]):
                # self.backStatusPrint(backTrack)
                print(f"\n\nbackTrack<---{self.player.currentRoom.room_id}: {self.player.currentRoom.name} - moves: {self.player.currentRoom.exits} -{self.player.currentRoom.description} - error: {self.player.currentRoom.errors} - {self.player.currentRoom.items}\n{backTrack}")

                back = backTrack.pop()
                path.append(back)
                
                # move to next room                
                room = Room(self.player.post_move(back))
                self.player.currentRoom = room
                wait = self.player.currentRoom.cooldown
                sleep(wait)
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
            wait = self.player.currentRoom.cooldown
            sleep(wait)
        # print(self.mapped)
        print(path)
        print(self.saved_map)
        return path
