#!/usr/bin/env python3

'''
Author: Bourguignon Maxime
'''

import matplotlib.pyplot as plt
from datetime import datetime


db = dict()

with open("loadbalancer.log", "r") as logfile:
    for line in logfile.read().splitlines():
        data = line.split(',') 
        print(data)
        time = data[0]
        idx = int(data[1])
        query = data[2]

        if time in db.keys():
            pass
        else:
            db[time] = dict()
            db[time]["post"] = [0,0,0]
            db[time]["get"] = [0,0,0]
        
        db[time][query][idx] += 1

data_post_0 = [ db[idx]["post"][0] for idx in db.keys()]
data_post_1 = [ db[idx]["post"][1] for idx in db.keys()]
data_post_2 = [ db[idx]["post"][2] for idx in db.keys()]
data_get_0 = [ db[idx]["get"][0] for idx in db.keys()]
data_get_1 = [ db[idx]["get"][1] for idx in db.keys()]
data_get_2 = [ db[idx]["get"][2] for idx in db.keys()]

data_post = [data_post_0, data_post_1, data_post_2]
data_get = [data_get_0, data_get_1, data_get_2]
axe_x = [ datetime.strptime(time, '%M-%S') for time in db.keys()]

palette=plt.get_cmap('Set1')

for i in range(3):
    
    plt.subplot(2, 3, i+1)
    for row in data_post:
        plt.plot(axe_x, row, marker='', color='grey', linewidth=0.6, alpha=0.3)
    plt.plot(axe_x, data_post[i], marker= '', color=palette(i), linewidth=1.2, alpha=0.9)

    plt.title("Post in DB_" + str(i), loc='left', color=palette(i))
    
    plt.subplot(2, 3, i+1+3)
    for row in data_get:
        plt.plot(axe_x, row, marker='', color='grey', linewidth=0.6, alpha=0.3)
    plt.plot(axe_x, data_get[i], marker= '', color=palette(i), linewidth=1.2, alpha=0.9)

    plt.title("Get in DB_" + str(i), loc='left', color=palette(i))

plt.show()

if __name__ == '__main__':
    pass
