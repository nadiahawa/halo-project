import json
from flask import Blueprint, jsonify, request
from app.api.services import token_required
api = Blueprint('api', __name__, url_prefix='/api')
from app.models import Character,db, User
from .services import token_required



@api.route('/test', methods=['GET'])
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
    return jsonify(characters), 200


@api.route('/characters/<string:name>', methods=['GET'])
def getCharactersName(name):
    print(name)
    character = Character.query.filter_by(name=name).first()
    if character:
        return jsonify(character.to_dict()), 200
    return jsonify({'error': f'no such character with the name {name}'})



@api.route('/create', methods=['POST'])
def createCharacter():
    newdict=request.get_json()
    # print(newdict)
    c = Character(newdict)
    # print(c)
    db.session.add(c)
    db.session.commit()
    # print({'created': c.to_dict})
    # print(type(c))
    return str(200)

@api.route('/update/<string:id>', methods =['POST'])
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
def removeCharacter(id):
    character = Character.query.get(id)
    if not character:
        return jsonify({'Remove failed': f'No character with ID {id} in the database.'}), 404
    db.session.delete(character)
    db.session.commit()
    return jsonify({'Removed character': character.to_dict()}), 200