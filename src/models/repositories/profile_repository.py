from typing import Dict
from pyodbc import Connection

class ProfileRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def find_profile_by_id(self, profile_id: str) -> Dict:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM Profiles WHERE id = ?''', (profile_id,)
        )
        profile = cursor.fetchone()
        return profile
    

    
   