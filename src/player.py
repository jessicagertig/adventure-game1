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

  def drop_item(self, item):
    self.inventory.remove(item)
    Room.items.append(item)
