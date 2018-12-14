# encoding: utf-8
from datetime import datetime


class World(object):
    ''' World object'''
    def __init__(self, id, state_hash):
        self.id = id
        self.state_hash = state_hash

    def __str__(self):
        return "World [id]={0} [hash]={1}".format(self.id, self.state_hash)


class Action(object):
    '''Action object'''
    def __init__(self, id, world_id, state_hash, _type, value=None, timestamp=None):
        self.id = id
        self.world_id = world_id
        self.state_hash = state_hash
        self.type = _type
        self.value = value
        if not self.timesamp:
            self.timestamp = datetime.utcnow()


    def __str__(self):
        return "Action [id]={0}".format(self.id)


class ActionRepository:

    def __init__(self, db):
        self.db = db

    def get_by_hash(self, state_hash):
        pass
    
    def get_after(self, after_hash):
        pass


class WorldRepository:

    def __init__(self, db):
        self.db = db

    def get_by_hash(self, world_id, state_hash):
        pass

    def get_latest_state(self, world_id):
        pass
