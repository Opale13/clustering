#!/usr/bin/env python3

from pymongo import MongoClient
from datetime import datetime

"""
    DB MongoDB
    ----------
    ip = 51.91.157.95
    port = 27017, 27018, 27019
    pwd = root, root
"""

"""
    GRAPHANA
    --------
    ip = 51.91.157.95
    port = 3000
    pwd = 
"""



class LoadBalancer():
    
    def __init__(self):
        self.__dbs = []
        pass

    def _post(self, db, data):
        return db.group.insert_one(data).inserted_id

    def _get(self, db, data):
        return db.group.find_one(data)

    def _log(self, idx, data, style):
        with open("loadbalancer.log", "a") as logfile:
            now = datetime.now()
            time = "{:02d}-{:02d}".format(now.hour, now.minute)
            logfile.write(time + ',' + str(idx) + ',' + style + '\n')

        print(data)
        
    def connect(self, http):
        client = MongoClient(http)
        db = client.asocial_network
        self.__dbs.append(db)
     
    def post(self, data):
        if "author" in data.keys():
            pass
        else:
            data["author"] = ""
        idx = len(data["author"]) % len(self.__dbs)
        db = self.__dbs[idx]
        result = self._post(db, data)
        self._log(idx, data, "post")
        return result

    def get(self, data):
        if "auhtor" in data.keys():
            pass
        else:
            data["author"] = ""
        idx = len(data["author"]) % len(self.__dbs)
        db = self.__dbs[idx]
        result = self._get(db, data)
        self._log(idx, data, "get")
        return result

if __name__ == '__main__':
    pass
