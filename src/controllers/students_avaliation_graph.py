from typing import Dict

class StudentsAvaliationGraph:
    def __init__(self, students_avaliation_repository, profile_repository, courses_repository) -> None:
        self.__students_avaliation_repository = students_avaliation_repository
        self.__profile_repository = profile_repository
        self.__courses_repository = courses_repository

        # Lista de habilidades
        self.__hard_skills = {}
        self.__soft_skills = {'communication': 0, 'teamwork': 0, 'leadership': 0, 'daptability': 0, 'problem solving': 0, 'time management': 0,
                            'creativity': 0, 'emotional intelligence': 0, 'critical thinking': 0, 'conflict resolution': 0, 'decision-making': 0,
                            'collaboration': 0, 'empathy': 0, 'resilience': 0, 'flexibility': 0, 'networking': 0, 'negotiation': 0, 'presentation skills': 0,
                            'listening': 0, 'initiative': 0}


    def find_avaliations(self, profile_id) -> Dict:
        try:
            self.set_hard_skills()
            avaliations = self.__students_avaliation_repository.find_avaliations_by_id(profile_id)
            profile = self.__profile_repository.find_profile_by_id(profile_id)
            if not avaliations: raise Exception("No Avaliations Found") 
            if not profile: raise Exception("No Profile Found") 

            for avaliation in avaliations:
                comment = avaliation[3]
                self.verify_hard_soft(comment)
            
            self.verify_hard_soft(profile[4])

            
            return {
                "body":{ 
                    "hard_skills" : self.__hard_skills,
                    "soft_skills" : self.__soft_skills
                },
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400 
            }
        
    def set_hard_skills(self) -> None:
        courses = self.__courses_repository.get_courses()
        for course in courses:
            name = course[1].lower()
            self.__hard_skills[name] = 0

    def verify_hard_soft(self, comment: str) -> None:
        for skill in self.__hard_skills:
            if skill in comment.lower():
                self.__hard_skills[skill] += 1
        for skill in self.__soft_skills:
            if skill in comment.lower():
                self.__soft_skills[skill] += 1
            
        