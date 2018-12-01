from pymongo import MongoClient

class Player:
    """Player class"""

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        info = "User %s", self.name
        return info

    def __repr__(self):
        return "User"


class Room:
    """ Room class"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        info = "Room %s", self.name
        return info

    def __repr__(self):
        return "Room"


class RoomRepository(object):
    """ Repository for CRUD operations on room collection in MongoDB """
    #TODO: refactor client, add indexes, add update and bulk insert actions

    def __init__(self, url, dbname):
        self.client = MongoClient(url)
        self.db = self.client[dbname]
        self.rooms = self.db['room']

    def create(self, room):
        '''
            Save new room in mongo
        :param room:
        :return:
        '''
        if room is not None:
            self.rooms.insert(room)
        else:
            raise ValueError("Please provide room object")

    def get(self, room_name):
        '''
        Get one or list of all rooms
        :param room_name:
        :return:
        '''
        if room_name is None:
            #Get all rooms
            return self.rooms.find()
        else:
            return self.rooms.find_one({"name": room_name})

    def delete(self, room):
        '''
        Delete room by id .
        :param room_id:
        :return:
        '''
        if room is not None:
            # In case the remove() method is invoked with empty parameter a
            # all the documents from the collection will be deleted.
            self.rooms.remove(room)
        else:
            raise Exception(
                "Nothing to delete, please provide room object")
