# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name,current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    

    def add_item(self,item):
       
        for i, e in enumerate(self.current_room.items):
            if e.name == item:
                
                self.inventory.append(e)
                
                self.current_room.remove_item(i)
        
    def get_item(self, item):
        for i in self.inventory:
            if i.name == item:
                return i


    def drop_item(self,item):
        for e, i in enumerate(self.inventory):
            if i.name == item:
                self.inventory.remove(i)
    
    