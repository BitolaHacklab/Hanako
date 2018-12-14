# encoding: utf-8


class World(object):
    ''' World object'''
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "World [id]={0} [name]={1}".format(self.id, self.name)


class Action(object):
    '''Action object'''
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "Action [id]={0} [name]={1}".format(self.id, self.name)
