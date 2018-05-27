from pymongo import *
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError


class MongoManager:
    def __init__(self, host='localhost'):
        self.connection = MongoClient(host)
        try:
            self.connection.server_info()
        except ServerSelectionTimeoutError as err:
            print(err)
        finally:
            pass


