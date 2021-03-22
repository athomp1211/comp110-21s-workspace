"""Examples of dictionaries."""

# Establish a type with dict[key type, value type]
# Empty dictionary literal is {}
players: dict[str, int] = {}

# Insert a new key-value pair
# Reference keys inside subscription notation, associated values are assigned
players["Brooks"] = 15
players["Love"] = 2
players["Bacot"] = 4
players["Bacot"] += 1 # Mutates value
print(players)
print(players["Brooks"])

# for...in loops will give you each key one-by-one
for player_name in players:
    key: str = player_name #*
    value: int = players[key] #*
    print(f"{player_name} -> {players[player_name]}")
    print(f"{key} -> {value}") #*
    #* for...in loops do these automatically


# You can have keys and values of any type! Notice this is the opposite mapping
# that we had above. Adiitionally this is an example of a dictionary literal.
jerseys: dict[int, str] = {15: "Brooks", 2: "Love", 5: "Bacot"}
jerseys[23] = "Jordan"
print(jerseys)
print(jerseys[23])

# The pop method allows you to remove a key-value pair by its key. The pop
# method returns the value associated with the popped key.
popped_names: str = jerseys.pop(23)
print(popped_names)
print(jerseys)
