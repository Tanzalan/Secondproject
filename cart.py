import json
def get_cart():
	cart = []
	with open('data/cart.json') as file:
		cart = json.load(file)
	return cart

#  Sort is a built in function call sorted


# import json

# def open_cart()
# with open('cart.json') as file:
# 	cart = json.load(file)

# def get_cart():
# 	cart = open_cart()
# 	cart = None
# 	for cart in cart:
# 		if pet['id'] == id:
# 			new_cart = pet 
# 	return cart.append(pet)
	
# def main():
#     data = []
#     for filename in glob.iglob('*.html'):
#         with open(filename) as f:
#             soup = BeautifulSoup(f)

#             title = soup.find("span", id="btAsinTitle")
#             data.append({
#                 "title":  title.get_text(),
#                 "author": title.find_next("a", href=True).get_text(),
#                 "isbn":   soup.find('b', text='ISBN-10:').next_sibling,
#                 "weight": soup.find('b', text='Shipping Weight:').next_sibling,
#                 "price":  soup.findAll('span', {"class":'bb_price'})
#             })

#     with open("my_output.json", "w") as outf:
#         json.dump(data, outf)

# main()
# Ask Solal or Yair what the significance of th "w" is...
def save_cart(data):
	with open("data/cart.json", "w") as file:
		json.dump(data, file)
	# return cart



def get_cart_total(cart):
	cart = save_cart([])
	total = 0
	for pet in cart:
		if "price" in pet and int(pet["price"]) > 0:
			total = int(total) + int(pet["price"])


	return total









