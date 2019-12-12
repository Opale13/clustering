import pymongo
from threading import Thread

def flood_database(db):
        print("coucou")

        posts = list()

        for i in range(0, 10):
                posts.append({
                        "author": "Guide of galactic traveler",
                        "message": "The answer is 42"
                })

        db.ludovic_collection.insert_many(posts).inserted_ids
        

if __name__ == '__main__':
        jobs = list()
        
        client = pymongo.MongoClient("mongodb+srv://Ludovic:Vv3t0Jc9PZd4Q7d7@commetuveux-cwxjt.mongodb.net/test?retryWrites=true&w=majority")
        db = client.asocial_network

        thread_pool = 3

        if thread_pool >= 0:
                thread = Thread(target=flood_database, args=(db,))
                jobs.append(thread)
                thread.start()

                thread_pool -= 1

        for job in jobs:
                job.join()
        
        jobs.clear()
        