from typing import Dict, List
from pyodbc import Connection

class CoursesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def get_courses(self) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute(
            ''' SELECT * FROM courses '''
        )
        courses = cursor.fetchall()
        return courses
    
    def get_course_by_id(self, course_id) -> Dict:
        cursor = self.__conn.cursor()
        cursor.execute(
            ''' SELECT * FROM courses WHERE id = ?''', (course_id,)
        )
        course = cursor.fetchone()
        return course
    

    
   