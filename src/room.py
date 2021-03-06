# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name,description):
        self.name = name;
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
    
    def get_item(self, item):
        for i in self.items:
            if i.name == item:
                return i
    
    def remove_item(self, item):
        for e, i in enumerate(self.items):
            if i.name == item:
                self.items.remove(i)