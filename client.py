'''
Author: Merel Ludovic
'''

from pymongo import MongoClient
from threading import Thread
from pprint import pprint
from requests import post, get
from random import randint, choice
import string
import json

THREAD_RANGE = 100
THREAD_POOL = 4
IP_LOAD_BALANCER = None

with open('config.json') as json_file:
    data = json.load(json_file)
    IP_LOAD_BALANCER = data["ip_load_balancer"]
    THREAD_RANGE = data["thread_range"]
    THREAD_POOL = data["thread_pool"]


def _randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(choice(letters) for i in range(stringLength))


def send_post():
    for i in range(THREAD_RANGE):
        if randint(0,1):
            post("http://{}:5000/post".format(IP_LOAD_BALANCER), json={
                    "id": randint(0, 2),
                    "author": _randomString(randint(0, 10)),
                    "message": _randomString(randint(0, 10))
                })
        
        else:
            post("http://{}:5000/get".format(IP_LOAD_BALANCER), json={
                    "id": randint(0, 2),
                    "author": _randomString(randint(0, 10)),
                    "message": _randomString(randint(0, 10))
                })


if __name__ == '__main__':

    jobs = list()

    i = 0
    while i < THREAD_POOL:
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
