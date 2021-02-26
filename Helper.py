import sqlite3 as sq
import json
import time

class Tlist(object):
    shuju=sq.connect("./shuju.db")
    cu=shuju.cursor()
    cu.execute("create table task(title text,sort text,deadline real,chain text,note text);")
    #创建数据库

    def tlist(self):
        cu=Tlist.cu
        sort=input("[sort]>")
        title=input("[title]>")
        deadline=input("[deadline]>")
        sql1='insert into task (title,sort,deadline) values ('f"title"','f"sort"','f"deadline"')'
        cu.execute(sql1)

    def tchain(self,chaintasks):
        pass

    def remove_task(self,t_to_rm):
        pass


class Stat(object):
    with open('stat.json','r+') as f:
        stat=json.load(f)
   
    def my_streak(self): 
        mode=input("[streak]>")
        if mode=="show":
            print("your streak is: ",Stat.stat["streak"])


        elif mode=="add":
            Stat.stat["streak"] += 1
            with open('stat.json','r+') as f:
                json.dump(Stat.stat,f)

        else:
            print("error")


    def point(self): 
        mode=input("[point]>")
        if mode=="show":
            print("your point is: ",Stat.stat["point"])

        elif mode=="add":
            Stat.stat["point"] += 1
            with open('stat.json','r+') as f:
                json.dump(Stat.stat,f)

        elif mode=="del":
            Stat.stat["point"] -= 1
            with open('stat.json','r+') as f:
                json.dump(Stat.stat,f)

        else:
            print('error')
                  
    def tomato(self):
        mode=input("[tomato]>")
        if mode == "start":

class Core(object):

    def default_state(self):
        pass

    def shift_mode(self,mode):
        pass



digua=Stat()
digua.my_streak()
digua.point()


