import sqlite3

class configdb:
    #con = None
    def __init__(self) -> None:
        self.con=sqlite3.connect("config.db")
        
    def get(self,id):
        res=self.con.execute("select value from config where id='" + id + "'")
        return res.fetchone()
    
    def all(self):
        res=self.con.execute("select id,value,desc from config ")
        return res.fetchall()
    
    def update(self,id,value):
        self.con.execute("update config set value='"+ value+"' where id='"+ id+"'")
        self.con.commit()
        
    def insert(self,id,value):
        self.con.execute("insert into config values('"+id+"','"+value+"','')")
        self.con.commit()
        
    def getConfig(self):
        config={}
        values=self.all()
        for val in values:
             config[val[0]]=val[1]
        return config
