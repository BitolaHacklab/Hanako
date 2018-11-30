from flask import Blueprint

room_api = Blueprint('room_api', __name__)

@room_api.route('/api/v1/rooms', methods=['POST'])
def create_room():
    return ''

@room_api.route('/api/v1/rooms', methods=['GET'])
def get_rooms():
    return ''

@room_api.route('/api/v1/rooms/<room_id>', methods=['GET'])
def get_room(room_id):
    return room_id

@room_api.route('/api/v1/players/<room_id>', methods=["PUT"])
def update_room(room_id):
    return room_id

@room_api.route('/api/v1/players/<room_id>', methods=['DELETE'])
def delete_room(room_id):
    return room_id

