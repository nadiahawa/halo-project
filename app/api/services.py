
from flask import request, jsonify
from functools import wraps
from app.models import User

def token_required(api_route):
    @wraps(api_route)
    def decorator_function(*args, **kwargs):
        token = request.headers.get('halo-access-token')
        if not token:
            return jsonify({'access denied = no API token'}), 401
        if not User.query.filer_by(api_token=token).first():
             return jsonify({'invalid api = api token incorrect'}), 403
        return api_route(*args, **kwargs) 
    return decorator_function

# def charactercardinfo():
#     character_api = request.get('http://127.0.0.1:5000/api/characters')        
#     if character_api.status_code == 200:
#         character_data = character_api.json()
#     else:
#         return 'broken api'
#     char_name = character_data['170075cf-dff0-4aac-83f0-9f3fc1cff6b3']['name']
#     char_affiliation = character_data['170075cf-dff0-4aac-83f0-9f3fc1cff6b3']['affiliation']
#     char_species = character_data['170075cf-dff0-4aac-83f0-9f3fc1cff6b3']['species']
#     char_image = character_data['170075cf-dff0-4aac-83f0-9f3fc1cff6b3']['image']
#     # id = character_data['170075cf-dff0-4aac-83f0-9f3fc1cff6b3']['id']
#     # creator = character_data['170075cf-dff0-4aac-83f0-9f3fc1cff6b3']['creator']

#     print(char_name)
#     print(char_affiliation)
#     print(char_image)
#     print(char_species)
#     # print(creator)
#     # print(id)


#     # name = [character_data[]['name']]
#     # return name 
# charactercardinfo()