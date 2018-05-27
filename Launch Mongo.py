import subprocess, os, shlex

class Mongo_Shell:
    def __init__(self, data_path):
        self.data_path = data_path

    def launch_mongodb(self, mongo_path):
        self.mongod = subprocess.Popen(shlex.split(mongo_path + 'mongod' +
                                                   " --dbpath {0}".format(os.path.expanduser(self.data_path))))
        self.test_connection = subprocess.Popen(shlex.split(mongo_path + 'mongo'))
        return self.mongod, self.test_connection


if __name__ == '__main__':
    path1 = '/Users/richardyang/Desktop/Research/mongodb/data/'
    path2 = '/Users/richardyang/Desktop/Research/mongodb/bin/'

    my_manager = Mongo_Shell(path1)
    my_manager.launch_mongodb(path2)