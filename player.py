class Player:

    def __init__(self, name, currentRoom, items=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.items = items

    def add_item(self, item):
        return self.items.append(item)
