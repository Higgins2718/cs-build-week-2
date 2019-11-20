from time import sleep
from room import Room


class Path:
    def __init__(self, player):
        self.player = player
        # create adjacency list with room as key and exits array as value
        self.mapped = dict()
        self.saved_map = []

    def dfs(self):
        path = []
        backTrack = []

        # {0: ['n', 's', 'w', 'e']}
        self.mapped[self.player.currentRoom.room_id] = self.player.currentRoom.exits
        # graph consisting of 500 rooms
        sleep(2)
        while len(self.mapped) < 499:
            
            sleep(2)
            
            room = self.player.currentRoom
            print(f"\n\n{room.room_id}: {room.name} - {room.description}")
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
                self.player.post_move(back)
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

            self.player.post_move(move)
            wait = self.player.currentRoom.cooldown
            sleep(wait)
        # print(self.mapped)
        print(path)
        print(self.saved_map)
        return path
