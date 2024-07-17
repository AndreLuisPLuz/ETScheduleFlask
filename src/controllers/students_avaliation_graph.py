from typing import Dict

class StudentsAvaliationGraph:
    def __init__(self, students_avaliation_repository, profile_repository, courses_repository) -> None:
        self.__students_avaliation_repository = students_avaliation_repository
        self.__profile_repository = profile_repository
        self.__courses_repository = courses_repository

        # Lista de habilidades
        self.__hard_skills = {}
        self.__soft_skills = {  
                                'Interpersonal and Communication': 0,
                                'Critical Thinking and Problem Solving': 0,
                                'Self Management and Personal Efficiency': 0,
                                'Creative and Innovative': 0
                            }


    def find_avaliations(self, profile_id) -> Dict:
        try:    
            self.set_hard_skills()
            avaliations = self.__students_avaliation_repository.find_avaliations_by_id(profile_id)
            profile = self.__profile_repository.find_profile_by_id(profile_id)
            if not avaliations: raise Exception("No Avaliations Found") 
            if not profile: raise Exception("No Profile Found") 

            for avaliation in avaliations:
                comment = avaliation[3]
                self.verify_hard_soft(comment.lower().replace(",", "").replace(".", "").split(' '))
            
            self.verify_hard_soft(profile[4].lower().replace(",", "").replace(".", "").split(' '))

            
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
        interpersonal_communication = ['communication', 'teamwork', 'leadership', 'adaptability', 'emotional intelligence', 'empathy', 'networking', 'collaboration', 
            'conflict resolution', 'negotiation', 'presentation skills', 'active listening', 'diplomacy', 'persuasion', 'interpersonal skills', 'relationship building']

        critical_thinking_problem_solving = ['problem solving', 'critical thinking', 'decision-making', 'analytical thinking', 'logical reasoning', 'strategic thinking', 'innovation']

        self_management_personal_efficiency = [ 'time management', 'resilience', 'flexibility', 'initiative', 'stress management', 'goal setting', 'self-motivation', 'adaptability']

        creative_innovative = ['creativity','design thinking','imagination','artistic skills','problem sensitivity']
        

        for word in comment:
            if word in interpersonal_communication:
                self.__soft_skills['Interpersonal and Communication'] += 1
            elif word in critical_thinking_problem_solving:
                self.__soft_skills['Critical Thinking and Problem Solving'] += 1
            elif word in self_management_personal_efficiency:
                self.__soft_skills['Self Management and Personal Efficiency'] += 1
            elif word in creative_innovative:
                self.__soft_skills['Creative and Innovative'] += 1
        
        for skill in self.__hard_skills:
            if skill in comment:
                self.__hard_skills[skill] += 1
        