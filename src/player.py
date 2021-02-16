# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, items):
        self.name=name
        self.location=location
        self.items=items
    def __str__(self):
        inventory=""
        for item in self.items:
            inventory= inventory + " " + item + "|"
        return f"name: {self.name}, location: {self.location}, items:{inventory}"
    def get_location(self):
        return self.location
    def check_items(self):
        return self.items
    def take_items(self, recieved):
        # for item in recieved:
        # print(recieved)
        self.items.append(recieved)
        return print(f"picked up {recieved.name}")
    def drop_item(self, recieved):
        dropping=""
        for index, item in enumerate(self.items):
            if recieved == item.name:
                dropping = item
                del self.items[index]
                return dropping