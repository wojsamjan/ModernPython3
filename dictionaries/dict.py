stan = {"name": "Stan", "age": 24}
print(stan)

yashi = dict(name = "Yashi", age = 24)
print(yashi)


# values, keys, items
wojtek = {"name": "Wojtek", "last_name": "Januszek", "age": 24}

for v in wojtek.values():
	print(f"value: {v}")

for k in wojtek.keys():
	print(f"key: {k}")

for k, v in wojtek.items():
	print(f"key: {k}, value: {v}")


# clear, copy, fromkeys, get
#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0.  Save the result to a variabled called initial_game_state
initial_game_state = dict.fromkeys(game_properties, 0)
print(initial_game_state)

# clear
initial_game_state.clear()
print(initial_game_state)

# copy, get
brother = dict(name = "Maciek", age = 24)
print(f"brother: {brother}")

name = brother.get("name")
last_name = brother.get("last_name")
print(f"Brother's name: {name}")
print(f"Brother's last_name: {last_name}")

me = brother.copy()
print(f"me: {me}")


# pop, popitem, update
stlv = {"name": "Caroline", "age": 24, "university": "PG", "city": "Gdańsk"}
print(f"St lo: {stlv}")

stlv.pop('university')
print(f"St lo: {stlv}")

stlv.popitem()  # pops random key-value pair
print(f"St lo: {stlv}")

stlv.update({"hate4ever": "me"})
print(f"St lo: {stlv}")
