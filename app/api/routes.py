import json
from tabnanny import check
from flask import Blueprint, jsonify, request
from app.api.services import token_required
api = Blueprint('api', __name__, url_prefix='/api')
from app.models import Cartitems, Character,db, User, Cart, Special, Vehicles
from .services import token_required
from flask_cors import CORS, cross_origin
from werkzeug.security import check_password_hash
# import stripe
# import os



@api.route('/test', methods=['GET'])
@cross_origin()
def test():
    x = Character.query.all()
    return jsonify('testing'), 200




@api.route('/characters', methods=['GET'])
def getCharacters():
    characters = Character.query.all()
    for c in characters:
        if User.id == Character.creator:
            print(characters)
    characters = {c.id:c.to_dict() for c in characters}
    response = jsonify(characters)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200
    #this is to help with CORS 


@api.route('/cart', methods=['GET'])
@cross_origin()
def getCart():
    # json_req = request.get_json()
    id = request.args['id']
    # print(json_req['id'])
    # get_cart = Cart.query.get(id)
    # print(get_cart)
    # response = jsonify(get_cart)
    response = {}
    print(id)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

@api.route('/cart/items', methods=['GET'])
@cross_origin()
def getCartItems():
    id = request.args['id']
    items = Cartitems.query.filter_by(cart=id)
    whole_cart = []
    total_cost = 0
    for i in items:
        item_type = i.item_type
        whole_cart.append(i.to_dict())
        if item_type == 'Weapon':
            weapon = Character.query.filter_by(name=i.item).first()
            total_cost += weapon.price
        if item_type == 'Special':
            special = Special.query.filter_by(name=i.item).first()
            total_cost += special.price
        if item_type == 'Vehicle':
            vehicle = Vehicles.query.filter_by(name=i.item).first()
            total_cost += vehicle.price
    print(whole_cart)
    total_cost_dict = {}
    total_cost_dict['total_cost'] = total_cost
    whole_cart.append(total_cost_dict)
    response = jsonify(whole_cart)
    # print(id)
    return response, 200
    # given cart id-done
    # query cart-items table where cart=id
    # for loop through the results, if result.type = 'weapon' query weapons table for cart_items.item
    # add each cart_items to dictionary
    # should be a dictionary like  this: "weapons": [weapon.name, weapon.name2, weapon.name3] "vehichles": [vehichle.name, vehicle.name2, etc]
    # keep a running tab of cost so every time you loop through an item add item.cost to total_cost



# @app.route('/cart/<int:product_id>', methods=['POST'])
# def add_to_cart(product_id):

#     product = Product.query.filter(Product.id == product_id)
#     cart_item = CartItem(product=product)
#     db.session.add(cart_item)
#     db.session.commit()


@api.route('/characters/<string:name>', methods=['GET'])
@cross_origin()
def getCharactersName(name):
    print(name)
    character = Character.query.filter_by(name=name).first()
    if character:
        return jsonify(character.to_dict()), 200
    return jsonify({'error': f'no such character with the name {name}'})



# @api.route('/create', methods=['POST'])
# @cross_origin()
# def createCart():
#     newdict=request.get_json()
#     # print(newdict)
#     c = Cart(newdict)
#     # print(c)
#     db.session.add(c)
#     db.session.commit()
#     # print({'created': c.to_dict})
#     # print(type(c))
#     return str(200)

@api.route('/update/<string:id>', methods =['POST'])
@cross_origin()
def updateCharacter(id):
    try:
        newvals = request.get_json()
        character = Character.query.get(id)
        character.from_dict(newvals)
        db.session.commit()
        return jsonify({'Updated character': character.to_dict()}), 200
    except:
        return jsonify({'Request failed': 'Invalid request or character ID does not exist.'}), 400

@api.route('/delete/<string:id>', methods=['DELETE'])
@cross_origin()
def removeCharacter(id):
    character = Character.query.get(id)
    if not character:
        return jsonify({'Remove failed': f'No character with ID {id} in the database.'}), 404
    db.session.delete(character)
    db.session.commit()
    return jsonify({'Removed character': character.to_dict()}), 200


@api.route('/signin', methods=['GET', 'POST'])
@cross_origin()
def getUser():
    json_req = request.get_json()
    print(json_req['username'])
    check_user = User.query.filter_by(username=json_req['username']).first()
    print(check_user)
    if check_user and check_password_hash(check_user.password, json_req['password']):
        print('success')
    # print(username, password)
        print(check_user)
        response = jsonify({'User': check_user.to_dict()})
        return response, 200
    return {}, 401 


# stripe.api_key = os.environ.get('STRIPE_SECRET')