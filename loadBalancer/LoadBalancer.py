#!/usr/bin/env python3

from pymongo import MongoClient
from datetime import datetime
from influxdb import InfluxDBClient
import json

class LoadBalancer():
    
    def __init__(self):
        self.__dbs = []

        self.__influxdb_host = ""
        self.__influxdb_port = 8086
        self.__influxdb_username = ""
        self.__influxdb_psw = ""

        self._read_json()
        self.__influxdb = InfluxDBClient(
            host=self.__influxdb_host, 
            port=self.__influxdb_port, 
            username=self.__influxdb_username, 
            password=self.__influxdb_psw, 
            ssl=False, 
            verify_ssl=False)

        self.__influxdb.switch_database('asocialnetwork')

        self.__query = {
            "measurement": "mongodb",
            "tags": {
                "database": ""
            },
            "fields": {
                "method": ""
            }
        }

    def _read_json(self):
        with open('config.json') as json_file:
            data = json.load(json_file)
            self.__influxdb_host = data["ip_server"]
            self.__influxdb_port = data["influxdb"]["ports"][0]
            self.__influxdb_username = data["influxdb"]["credentials"]["user"]
            self.__influxdb_psw = data["influxdb"]["credentials"]["password"]

    def _post(self, db, data):
        self.__query["tags"]["database"] = str(self.__dbs.index(db));
        self.__query["fields"]["method"] = "post"
        self.__influxdb.write_points([self.__query])

        return db.group.insert_one(data).inserted_id

    def _get(self, db, data):
        self.__query["tags"]["database"] = str(self.__dbs.index(db));
        self.__query["fields"]["method"] = "get"
        self.__influxdb.write_points([self.__query])

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
