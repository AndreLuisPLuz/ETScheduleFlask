from typing import Dict

class StudentsAvaliationFinder:
    def __init__(self, students_avaliation_repository, profile_repository) -> None:
        self.__students_avaliation_repository = students_avaliation_repository
        self.__profile_repository = profile_repository

    def find_avaliations(self, profile_id) -> Dict:
        try:
            avaliations = self.__students_avaliation_repository.find_avaliations_by_id(profile_id)
            profile = self.__profile_repository.find_profile_by_id(profile_id)
            if not avaliations: raise Exception("No Avaliations Found") 

            formatted_avaliations = []

            for avaliation in avaliations:
                formatted_avaliations.append({
                    "id": avaliation[0],
                    "discipline_id": avaliation[1],
                    "comment": avaliation[3]
                })
            return {
                "body":{ 
                    "consensus" : profile[3],
                    "avaliations" : formatted_avaliations
                },
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400 
            }