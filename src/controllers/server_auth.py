
class ServerAuth:
    def __init__(self, users_repository) -> None:
        self.__users_repository = users_repository
        self.__token

    def auth(self, login: str, password: str):

        users = self.__users_repository.get_users()

        for user in users:
            if user[1] == login:
                hashed_password = user[4]

                


