'''Collection of tools to make it easier to work with MongoDB
'''

from pymongo import MongoClient

class MongoCollection(object):
    '''Connect to mongodb and return collection within context manager
    '''

    def __init__(self, uri, collection):
        self.client = MongoClient(uri)
        self.db = self.client.get_default_database()
        self.collection = self.db[collection]

    def __enter__(self):
        return self.collection

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()
