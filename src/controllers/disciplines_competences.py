from typing import Dict
import numpy as np

class DisciplinesCompetencesGraph:
    def __init__(self, profile_repository, disciplines_repository, competences_repository, courses_repository, student_competences_repository) -> None:
        self.__profile_repository = profile_repository
        self.__disciplines_repository = disciplines_repository
        self.__competences_repository = competences_repository
        self.__courses_repository = courses_repository
        self.__student_competences_repository =student_competences_repository


    def find_disciplines_competences(self, profile_id) -> Dict:
        try:
            all_disciplines_infos = []
            

            profile = self.__profile_repository.find_profile_by_id(profile_id)
            if not profile: raise Exception("No Profile Found")
            disciplines = self.__disciplines_repository.get_disciplines_from_group(profile[2])
            if not disciplines: raise Exception("No Disciplines Found")

            for discipline in disciplines:
                discipline_info = {}
                competences_info = {}
                competences_average = 0

                course = self.__courses_repository.get_course_by_id(discipline[4])
                competences = self.__competences_repository.get_competences_from_disciplines(discipline[0])
                if not course: raise Exception("No Course Found")
                if not competences: raise Exception("No Competences Found")
                discipline_name = str(course[1])

                competence_values = [] 
                competence_weights = []  

                for competence in competences:
                    student_competences = self.__student_competences_repository.find_competences_by_student_competence(profile[0], competence[0])
                    if not student_competences: raise Exception("No Students Competences Found")

                    weight = competence[3]
                    degree = student_competences[3]

                    if degree == 'apt':
                        competence_values.append(1)  
                        competence_weights.append(weight)
                    elif degree == 'progress':
                        competence_values.append(0.5) 
                        competence_weights.append(weight)
                    elif degree == 'inapt':
                        competence_values.append(0)
                        competence_weights.append(weight)

                competence_values = np.array(competence_values)
                competence_weights = np.array(competence_weights)

                if len(competence_values) > 0:  
                    competences_average = np.average(competence_values, weights=competence_weights)
                
                competences_info['semester'] = str(discipline[4])
                competences_info['competences_average'] = competences_average * 100

                discipline_info['discipline_name'] = discipline_name
                discipline_info['stats'] = competences_info

                all_disciplines_infos.append(discipline_info)
            
            return {
                "body":{ 
                    "disciplines" : all_disciplines_infos
                },
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400 
            }
 
        