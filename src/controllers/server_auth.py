from typing import Dict
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class ServerAuth:
    def __init__(self, users_repository) -> None:
        self.__users_repository = users_repository

    def firts_access(self, body) -> Dict:
        try:
            # Gerar hash da senha
            password_hash = generate_password_hash(body['password']).decode('utf-8')
            body['password'] = password_hash

            user_infos = { **body }

            self.__users_repository.insert_user(user_infos)

            return {
                "body": { "message": "Created with success." },
                "status_code": 201  #significa Criado com sucesso
            }
        
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400 
            }
        
    def login(self, body, ) -> Dict:
        try:
            user = self.__users_repository.get_user_by_username(body['username'])

            if not user: raise Exception("Username invalid") 
            
            if not check_password_hash(user[5], body['password']): 
                raise Exception("Password invalid") 

            # Gerar o token JWT
            access_token = create_access_token(identity=user[1])

            # Retornar o token JWT como resposta
            return {
                "body": { "token": access_token },
                "status_code": 200 
            }
            
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400 
            }


                


