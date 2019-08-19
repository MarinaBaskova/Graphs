opposite_directions = {
    "n": "s",
    "s": "n",
    "w": "e",
    "e": "w"
}


def traverse_recursively(player, visited_rooms):
    path = []
    exits = player.currentRoom.getExits()
    visited_rooms[player.currentRoom.id] = True

    for exit in exits:

        exit_room = player.currentRoom.getRoomInDirection(exit)

        if exit_room and not room_was_visited(exit_room, visited_rooms):
            player.travel(exit)
            path.append(exit)
            exit_room_path = traverse_recursively(player, visited_rooms)
            path.extend(exit_room_path)
            player.travel(opposite_directions[exit])
            path.append(opposite_directions[exit])

    return path


def room_was_visited(room, visited_rooms):
    return visited_rooms.get(room.id, False)
