from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

class PlayerRepo:

    def __init__(self, dburl, dbname):
        self.client = MongoClient(dburl)
        self.db = self.client[dbname]
        self.player_collection = self.db['player']

    #
    # Get One or More Players
    #
    def get(self, id=None, query=None, page=1, limit=PAGE_LIMIT):
        # Only one entry
        if id:
            result = self.player_collection.find_one({'_id': ObjectId(_id)})
            return json.dumps(result, default=json_util.default)

        # Multiple entries
        json_docs = []
        resultset = player_collection.find(query, skip=(page-1)*limit, limit=limit)
        for result in resultset:
            result_json = json.dumps(result, default=json_util.default)
            json_docs.append(result_json)

        return json_docs
   
    def save(self, player):
        return player_collection.save(player)