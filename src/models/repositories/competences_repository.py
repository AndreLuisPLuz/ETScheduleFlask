from typing import Dict, List
from pyodbc import Connection

class CompetencesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def get_competences(self) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute(
            ''' SELECT * FROM competences '''
        )
        competences = cursor.fetchall()
        return competences
    
    def get_competences_from_disciplines(self, discipline_id) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute(
            ''' SELECT * FROM competences WHERE discipline_id = ?''', (discipline_id,)
        )
        competences = cursor.fetchall()
        return competences


    

    
   