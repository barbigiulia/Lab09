from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor  = conn.cursor(dictionary=True)
        res = []
        query = """select *
                from  airports a 
        """
        cursor.execute(query)
        for row in cursor:
            res.append(Aeroporto(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getEdges(distanza_minima):
        conn = DBConnect.get_connection()
        cursor  = conn.cursor(dictionary=True)
        res = []
        query = """select a.ID as id1, a2.ID as id2 , AVG(f.DISTANCE ) as peso
                    from flights f
                    join airports a  
                    on f.ORIGIN_AIRPORT_ID =a.ID 
                    join airports a2 
                    on f.DESTINATION_AIRPORT_ID =a2.ID 
                    where  a.ID  < a2.ID 
                    group by  a.ID , a2.ID
                    having peso > %s
        """
        cursor.execute(query, (distanza_minima,))   # attenzione alle parentesi!!!
        for row in cursor:
            res.append((row["id1"], row["id2"], row["peso"]))

        cursor.close()
        conn.close()
        return res