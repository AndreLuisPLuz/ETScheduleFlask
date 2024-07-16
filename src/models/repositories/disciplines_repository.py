from typing import Dict, List
from pyodbc import Connection

class DisciplinesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def get_disciplines(self) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute(
            ''' SELECT * FROM disciplines '''
        )
        disciplines = cursor.fetchall()
        return disciplines
    
    def get_disciplines_from_group(self, group_id) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute(
            ''' SELECT * FROM disciplines WHERE group_id = ?''', (group_id,)
        )
        competences = cursor.fetchall()
        return competences
    

    
   