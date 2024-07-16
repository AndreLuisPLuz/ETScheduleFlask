from typing import Dict, List
from pyodbc import Connection

class StudentCompetencesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    
    def find_competences_by_student_competence(self, profile_id, competence_id) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM student_competences WHERE student_id = ? AND competence_id = ?''', (profile_id, competence_id,)
        )
        competences = cursor.fetchone()
        return competences
    
    

    
   