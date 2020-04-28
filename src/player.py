from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, location):
    self.location = location
    self.name = None
    self.inventory = []

  def get_item(self, item):
    self.inventory.append(item)
    self.location.items.remove(item)
    new_item = item.item_name.upper()
    print(f"You have added {new_item} to your inventory!\n")

  def drop_item(self, item):
    self.inventory.remove(item)
    self.location.items.append(item)
    dropped_item = item.item_name.upper()
    print(f"You have removed {dropped_item} from your inventory!\n")
