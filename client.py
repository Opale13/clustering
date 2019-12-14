'''
Author: Merel Ludovic
'''

from pymongo import MongoClient
from threading import Thread
from pprint import pprint
from requests import post, get
from random import randint, choice
import string

THREAD_RANGE = 100


def flood_database(db, start):
    for i in range(start * THREAD_RANGE, (start * THREAD_RANGE) + THREAD_RANGE):
        post = {
            "id": i,
            "author": "Guide of galactic traveler",
            "message": "The answer is 42"
        }

        db.ludovic_collection.insert_one(post)


def read_database(db):
    for i in range(0, THREAD_RANGE):
        pprint(db.ludovic_collection.find_one({"id": i}))


def _randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(choice(letters) for i in range(stringLength))


def send_post():
    for i in range(THREAD_RANGE):
        if randint(0,1):
            post("http://localhost:5000/post", json={
                    "id": randint(0, 2),
                    "author": _randomString(randint(0, 10)),
                    "message": _randomString(randint(0, 10))
                })
        
        else:
            post("http://localhost:5000/get", json={
                    "id": randint(0, 2),
                    "author": _randomString(randint(0, 10)),
                    "message": _randomString(randint(0, 10))
                })


if __name__ == '__main__':

    jobs = list()

    # client = pymongo.MongoClient("mongodb+srv://<username>:<psw>@commetuveux-shard-00-01-cwxjt.mongodb.net/test?retryWrites=true&w=majority")
    # db = client.asocial_network

    # db.ludovic_collection.drop()
    # db.ludovic_collection

    i, thread_pool = 0, 3
    while i < thread_pool:
        # thread = Thread(target=flood_database, args=(db,i))
        # thread = Thread(target=read_database, args=(db,))
        thread = Thread(target=send_post)
        jobs.append(thread)
        thread.start()

        print("Thread number %d is run" % (i + 1), flush=True)

        i += 1

    print("\nWait jobs")
    for index, job in enumerate(jobs):
        job.join()
        print("Thread number %d is finished" % (index + 1), flush=True)

    jobs.clear()
