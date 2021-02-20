import sqlite3 as sq
import json

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
    with open('stat.json'.'w+') as f:
        json.load(f)
    
   
    def my_streak(self): #有bug，add不了
        mode=input("[streak]>")
        if mode=="show":

        elif mode=="add":

        else:
            print("error")


    def point(self): #有bug，add不了
        mode=input("[point]>")
        if mode=="show":

        elif mode=="add":

        elif mode=="del":

        else:
            print('error')
                  
    def tomato(self):
        pass

class Core(object):

    def default_state(self):
        pass

    def shift_mode(self,mode):
        pass


digua=Tlist()
digua.tlist()


