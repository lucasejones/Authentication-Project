import json

some_dict = {'kew': 'value'}

# makes a json version in a new file of what you pass into json.dumps
with open('data.txt', 'w') as file:
	file.write(json.dumps(some_dict))

print(some_dict)

# retrieves the json from the other file and converts back to original form
load_dict = {}
with open('data.txt', 'r') as file:
	text_data = file.read()
	load_dict = json.loads(text_data)

print(load_dict)




some_dict = {'key': 'value'}
with open('data.txt', 'w') as file:
	file.write(json.dumps(some_dict))

load_dict = {}
with open('data.txt', 'r') as file:
	text_data = file.read()
	load_dict = json.loads(text_data)