import json

with open('data/pets.json') as file:
	pets = json.load(file)

def find_pet(id):
	pets = get_pets()
	found_pet = None
	for pet in pets:
		if pet['id'] == id:
			found_pet = pet
	return found_pet


def get_pets():
	with open('data/pets.json') as file:
		pets = json.load(file)
	return pets

# def find_pet():
# 	pet_page = {}
# 	for pet in pets:
# 		if pet[id] == pet_id:
# 			pet_page = pet_id
# 		return pet_page



	return data

#...........................................

# def add_cart(id):
# 	q = q_q()
# 	q_q = None
# 	for q in q:
# 		if pet['id'] == id:
# 			found_pet = pet 
# 	return found_pet.append(id)
