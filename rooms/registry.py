room_scene_registry = {"Kitchen": None, "Engineering Table": None, "Bathroom": None}

def add_room(room, scene_class):
  room_scene_registry[room.name] = room
  room.scene = scene_class(room)
  return room
