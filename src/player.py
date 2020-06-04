from item import Item

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
            print("Inventory: ")
            for item in self.items:
                print(item.name)
    
    def pickup_item(self, item):
        if self.current_room.items.count(item) > 0:
            self.items.append(item)
            self.current_room.items.remove(item)
            item.on_take()
        else:
            return f"No items here"

    def drop_item(self, item):
        self.items.remove(item)
        self.current_room.items.append(item)
        item.on_drop()