import sqlite3 as sq

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
    
    txt=open("stat.txt",'r+') #要注意此处不清除文件
    content0=txt.readline()
    streak=int(content0)
    content1=txt.readline()
    points=int(content1)
    txt.close()
   
    def my_streak(self): #有bug，add不了
        mode=input("[streak]>")
        if mode=="show":
            txt=open("stat.txt",'r+')
            firstline=txt.readline()
            print("your streak is: ",firstline)
            txt.close()

        elif mode=="add":
            new_streak=Stat.streak + 1
            txt=open("stat.txt",'r+')
            txt.write(str(new_streak))
            txt.close()

        else:
            print("error")


    def point(self): #有bug，add不了
        mode=input("[point]>")
        if mode=="show":
            txt=open("stat.txt",'r+')
            firstline=txt.readline()
            secondline=txt.readline()
            print("your point is: ",secondline)
            txt.close()

        elif mode=="add":
            new_points=Stat.points + 1
            txt=open("stat.txt",'r+')
            txt.write(str(new_points))
            txt.close()

        elif mode=="del":
            new_points=Stat.points - 10
            txt=open("stat.txt",'r+')
            txt.write(str(new_points))
            txt.close()

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


