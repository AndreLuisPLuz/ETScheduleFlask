from typing import Dict, List
from pyodbc import Connection

class StudentAvaliationRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    
    def find_avaliations_by_id(self, profile_id) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM students_avaliation WHERE student_id = ?''', (profile_id,)
        )
        avaliations = cursor.fetchall()
        return avaliations
    
    

    
   