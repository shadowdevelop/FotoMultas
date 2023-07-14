import sqlite3

class reportdb:
    #con = None
    def __init__(self) -> None:
        self.con=sqlite3.connect("reporte.db")
        
    def get(self,id):
        res=self.con.execute("select id,fecha,velocidad,archivo from reporte where id='" + id + "'")
        return res.fetchone()
    
    def all(self):
        res=self.con.execute("select id,fecha,velocidad,archivo from reporte ")
        return res.fetchall()
    
    
    def insert(self,fecha,veloccidad,archivo):
        self.con.execute("insert into reporte values('"+fecha+"','"+veloccidad+"','"+archivo+"')")
        self.con.commit()
        
    def clear(self):
        self.con.execute("truncate table reporte")
        self.con.commit()
        

