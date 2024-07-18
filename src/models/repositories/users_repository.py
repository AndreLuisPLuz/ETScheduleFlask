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
    
    def get_user_by_username(self, username) -> Dict:
        cursor = self.__conn.cursor()
        cursor.execute( '''SELECT * FROM users WHERE username = ? ''', (username,) )
        user = cursor.fetchone()
        return user
    
    def insert_user(self, user_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute( 
            '''
                 INSERT INTO users
                    ( username, date_of_birth, full_name, [password])
                VALUES
                    (?, ?, ?, ?)
            ''' , (
                user_infos['username'],
                user_infos['date_of_birth'],
                user_infos['full_name'],
                user_infos['password']
            )
        )
        self.__conn.commit()
