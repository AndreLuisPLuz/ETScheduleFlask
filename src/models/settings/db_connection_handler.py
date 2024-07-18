import pyodbc
from pyodbc import Connection

class DbConnectionHandler:
    def __init__(self) -> None:
        self.__server = 'CA-C-0064X\SQLEXPRESS' #Nome do server 
        self.__database = 'ets_schedule' #Nome do Database
        
        self.__conn = None
        
    def connect(self) -> None:
        self.__conn = pyodbc.connect('  DRIVER={ODBC Driver 17 for SQL Server};\
                        SERVER='+self.__server+';\
                        DATABASE='+self.__database+';\
                        Trusted_Connection=yes') 
    
    def get_connection(self) -> Connection:
        #-> Connection: mostra que vou retorar um elemento do tipo connection
        return self.__conn
        
db_connection_handler = DbConnectionHandler()


