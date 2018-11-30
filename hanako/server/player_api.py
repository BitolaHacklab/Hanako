from flask import Blueprint

player_api = Blueprint('player_api', __name__)

@player_api.route('/api/v1/players', methods=['POST'])
def create_player():
    return ''

@player_api.route('/api/v1/players', methods=['GET'])
def get_players():
    return ''

@player_api.route('/api/v1/players/<player_id>', methods=['GET'])
def get_player(player_id):
    return player_id

@player_api.route('/api/v1/players/<player_id>', methods=["PUT"])
def update_player(player_id):
    return player_id

@player_api.route('/api/v1/players/<player_id>', methods=['DELETE'])
def delete_player(player_id):
    return player_id

@player_api.route('/api/v1/players/<player_id>/rooms', methods=['POST'])
def join_room(player_id):
    return player_id

@player_api.route('/api/v1/players/<player_id>/rooms', methods=['DELETE'])
def leave_room(player_id):
    return player_id
