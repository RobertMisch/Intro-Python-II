# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name=name
        self.description=description
        self.items=items
        self.n_to=None
        self.e_to=None
        self.s_to=None
        self.w_to=None
    def __str__(self):
        return (f"room: name: {self.name}| description: {self.description}").format(self=self)
    def get_description(self):
        return (self.description).format(self=self)
    def check_items(self):
        return self.items
    def take_items(self, taking):
        given_item=""
        # print(taking)
        for index, item in enumerate(self.items):
            # print(taking)
            # print(item)
            if(item.name == taking):
                given_item=item
                del self.items[index]
        return given_item
    def add_item(self, recieved):
        self.items.append(recieved)

