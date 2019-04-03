from flask import Flask
from flask import render_template, redirect, url_for

from cart import get_cart, save_cart, get_cart_total
from pets import get_pets, find_pet


app = Flask(__name__)
# Required URLs:
# /                 -> index page.
# /pets/            -> listing of all pets in the store
# /pets/3/          -> display the pet with the given ID (numerical)
# /cart/            -> display your cart
# /cart/add_pet/3/  -> add to your cart one pet with the given ID. redirect to /cart/
# /cart/empty/      -> empty your cart. redirect to /
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/pets/")
def show_pets():
	pets = get_pets()
	return render_template('pets.html', pets = pets)


# @app.route("/cart")
# def show_cart():
#     return render_template('cart.html')

@app.route("/pets/<id>/")
def show_pet(id):
	#This is the cup that catches the juice
	pet = find_pet(id)
	return render_template('pet.html', pet = pet)


# @app.route("/cart/add_pet/<id>")
# def cart_add():
# 	return render_template('cart.html')

@app.route("/cart/")
def show_cart():
	cart = get_cart()
	return render_template('cart.html', cart = cart)


@app.route("/cart/empty/")
def empty_cart():
	cart = save_cart([])
	total = get_cart_total(cart)

	return redirect(url_for("cart.html", cart = cart, total = total))

@app.route('/cart/add_pet/<id>/')
def add_to_cart(id):
	pet = find_pet(id)
	cart = get_cart()
	if pet is not None:
		cart.append(pet)
	save_cart(cart)	
	return redirect(url_for("show_cart"))






