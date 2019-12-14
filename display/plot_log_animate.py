import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

fig = plt.figure()

post_db = [fig.add_subplot(2,3,1), fig.add_subplot(2,3,2), fig.add_subplot(2,3,3)]

get_db0 = fig.add_subplot(2,3,4)
get_db1 = fig.add_subplot(2,3,5)
get_db2 = fig.add_subplot(2,3,6)

get_db = [get_db0, get_db1, get_db2]

def animate(i):
    db = dict()

    graph_data = open('loadbalancer.log','r').read()
    lines = graph_data.split('\n')
    for line in lines:
        if len(line) > 1:
            data = line.split(',') 
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
    data_post = [data_post_0, data_post_1, data_post_2]

    data_get_0 = [ db[idx]["get"][0] for idx in db.keys()]
    data_get_1 = [ db[idx]["get"][1] for idx in db.keys()]
    data_get_2 = [ db[idx]["get"][2] for idx in db.keys()]
    data_get = [data_get_0, data_get_1, data_get_2]

    axe_x = [ datetime.strptime(time, '%M-%S') for time in db.keys()]
    
    palette=plt.get_cmap('Set1')

    for i in range(3):
        post_db[i].clear()
        get_db[i].clear()

        for row_post, row_get in zip(data_post, data_get):
            post_db[i].plot(axe_x, row_post, marker='', color='grey', linewidth=0.6, alpha=0.3)
            get_db[i].plot(axe_x, row_get, marker='', color='grey', linewidth=0.6, alpha=0.3)

        post_db[i].plot(axe_x, data_post[i], marker= '', color=palette(i), linewidth=1.2, alpha=0.9)
        get_db[i].plot(axe_x, data_get[i], marker= '', color=palette(i), linewidth=1.2, alpha=0.9)

        post_db[i].set_title("Post in DB_" + str(i), loc='left', color=palette(i))
        get_db[i].set_title("Get in DB_" + str(i), loc='left', color=palette(i))

ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()