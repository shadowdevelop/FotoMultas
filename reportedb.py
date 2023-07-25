import sqlite3

class reportdb:
    #con = None
    def __init__(self) -> None:
        self.con=sqlite3.connect("reporte.db")
        
    def get(self,id):
        res=self.con.execute("select idx,fecha,velocidad,archivo,equipo from reporte where id='" + str(id) + "'")
        return res.fetchone()
    
    def all(self):
        res=self.con.execute("select idx,fecha,velocidad,archivo,equipo from reporte ")
        return res.fetchall()
    
    
    def insert(self,veloccidad,archivo,equipo):
        self.con.execute("insert into reporte(velocidad,archivo,equipo) values('"+str(veloccidad)+"','"+str(archivo)+"','"+str(equipo)+"')")
        self.con.commit()
        
    def clear(self):
        self.con.execute("truncate table reporte")
        self.con.commit()
        

