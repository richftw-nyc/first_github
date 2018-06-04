from pymongo import *
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import importlib

class MongoManager:
    def __init__(self, host='localhost'):
        self.connection = MongoClient(host)
        try:
            info = self.connection.server_info()
        except ServerSelectionTimeoutError as err:
            print(err)
            launch_mod = importlib.import_module("Launch Mongo")
            launch_mod.main()
        finally:
            print('server connected')
            self.connection.list_database_names()



# from imapidle import imaplib
#
# m = imaplib.IMAP4_SSL('imap.gmail.com')
# m.login('robert', 'pa55w0rd')
#
#


if __name__ == '__main__':
    test = MongoManager()