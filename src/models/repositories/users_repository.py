from typing import Dict, List
from pyodbc import Connection

class UsersRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def get_users(self) -> List[Dict]:
        cursor = self.__conn.cursor()
        cursor.execute( '''SELECT * FROM users ''' )
        users = cursor.fetchall()
        return users