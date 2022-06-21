from flask import request

def getallweapons():
    halo_api = request.get('http://127.0.0.1:5000/api/weapons')
    if halo_api.status_code == 200:
        halo_data = halo_api.json()
    else:
        return 'broken api'
    name = [v['name'] for v in halo_data]
    return name