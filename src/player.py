# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return f"Name: {self.name}, Room: {self.current_room}"

    def inventory(self):
        if not self.items:
            print("inventory empty")
        else:
            for item in self.items:
                return f"You are carrying: {item}" 
    
    def get_item(self, item):
        if len(self.current_room.items) > 0:
            self.items.append(item)
            self.current_room.items.remove(item)
            return f"You picked up {item}"
        else:
            return f"No items here"

    def drop_item(self, item):
        if len(self.item) > 0:
            self.items.remove(item)
            self.current_room.items.append(item)
            return f"You dropped {item}"