import os
from flask import Flask, Response

from hanako.server.player_api import player_api
from hanako.server.room_api import room_api

api = Flask(__name__)
api.register_blueprint(player_api)
api.register_blueprint(room_api)

@api.route('/health')
def health_check():
    return Response(os.uname())

@api.route('/api/v1/cqrs', methods=['POST'])
def cqrs():
    return ''
