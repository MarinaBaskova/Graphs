## Description

You are provided with a pre-generated graph consisting of 500 rooms. You are responsible for filling `traversalPath` with directions that, when walked in order, will visit every room on the map at least once.

Open `adv.py`. There are four parts to the provided code:

- World generation code. Do not modify this!
- An incomplete list of directions. Your task is to fill this with valid traversal directions.
- Test code. Run the tests by typing `python3 adv.py` in your terminal.
- REPL code. You can uncomment this and run `python3 adv.py` to walk around the map.

You may find the commands `player.currentRoom.id`, `player.currentRoom.getExits()` and `player.travel(direction)` useful.

To solve this path, you'll want to construct your own traversal graph. You start in room `0`, which contains exits `['n', 's', 'w', 'e']`. Your starting graph should look something like this:

```
{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}
```

Try moving south and you will find yourself in room `5` which contains exits `['n', 's', 'e']`. You can now fill in some entries in your graph:

```
{
  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': '?', 'e': '?'}
}
```

You know you are done when you have exactly 500 entries (0-499) in your graph and no `'?'` in the adjacency dictionaries. To do this, you will need to write a traversal algorithm that logs the path into `traversalPath` as it walks.

## Hints

There are a few smaller graphs in the file which you can test your traversal method on before committing to the large graph. You may find these easier to debug.

Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.

You can find the path to the shortest unexplored room by using a breadth-first search for a room with a `'?'` for an exit. If you use the `bfs` code from the homework, you will need to make a few modifications.

1. Instead of searching for a target vertex, you are searching for an exit with a `'?'` as the value. If an exit has been explored, you can put it in your BFS queue like normal.

2. BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.

If all paths have been explored, you're done!

## Minimum Viable Product

- **1**: Tests do not pass
- **2**: Tests pass with `len(traversalPath) < 2000`
- **3**: Tests pass with `len(traversalPath) < 1000`

## Stretch Problems

It is very difficult to calculate the shortest possible path that traverses the entire graph. Why?

My best path is 990 moves. Can you find a shorter path?

# DFT

# Request direction that you can move

# Make a move ( pick direction)

# Get current room id

# Set edges between last room and current room

# Request direction that you can move loop through them and add edges to the current room with availble directions from the request

# We are done when our keys in the Graph == 500

# STEPS TO SOLVE (almost) ANY GRAPHS PROBLEM!

# - Translate the problem into graph terminology

# Nodes: Rooms - each room has a number

# Edges: Exists N S E W that leads to that room

# Non directional

# DFT until we hit deadend and then call BFS

# - Build your graph

# - Traverse your graph
