from typing import List
from textblob import TextBlob

class StudentsAvaliationGraph:
    def __init__(self, students_avaliation_repository, profile_repository, courses_repository) -> None:
        self.__students_avaliation_repository = students_avaliation_repository
        self.__profile_repository = profile_repository
        self.__courses_repository = courses_repository

        # Lista de habilidades
        self.__hard_skills= [
                            {
                                'competence_name': 'Programming Languages',
                                'value': 0
                            },
                            {
                                'competence_name': 'Software Testing',
                                'value': 0
                            },
                            {
                                'competence_name': 'Web Development',
                                'value': 0
                            },
                            {
                                'competence_name': 'Desktop Development',
                                'value': 0
                            },
                            {
                                'competence_name': 'Databases',
                                'value': 0
                            },
                            {
                                'competence_name': 'Logic Programming',
                                'value': 0
                            },
                            {
                                'competence_name': 'Application Security',
                                'value': 0
                            },
                            {
                                'competence_name': 'Machine Learning',
                                'value': 0
                            },
                            {
                                'competence_name': 'Internet of Things',
                                'value': 0
                            }]
        self.__soft_skills = {  
                                'Communication': 0,
                                'Teamwork': 0,
                                'Initiative': 0,
                                'Leadership': 0,
                                'Organization': 0
                            }


    def find_avaliations(self, profile_id) -> List:
        try:    
            avaliations = self.__students_avaliation_repository.find_avaliations_by_id(profile_id)
            profile = self.__profile_repository.find_profile_by_id(profile_id)
            if not avaliations: raise Exception("No Avaliations Found") 
            if not profile: raise Exception("No Profile Found") 

            formatted_comment = []
            for avaliation in avaliations:
                comment = avaliation[3]
                comment = comment.lower().replace(",", "").split('.')
                for phrases in comment:
                    formatted_comment = phrases.split(' ')
                    if len(formatted_comment) < 2: continue
                    self.verify_soft_skills(formatted_comment)
                    self.verify_hard_skills(formatted_comment)
            
            formatted_concensus = profile[4].lower().replace(",", "").split(".")
            for phrases in formatted_concensus:
                formatted_comment = phrases.split(' ')
                if len(formatted_comment) < 2: continue
                self.verify_soft_skills(formatted_comment)
                self.verify_hard_skills(formatted_comment)

            
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

    def verify_soft_skills(self, comment: str) -> None:
        communication = [
            "verbal communication",
            "nonverbal communication",
            "active listening",
            "clear expression of ideas",
            "persuasion",
            "negotiation",
            "interpersonal communication",
            "constructive feedback",
            "written communication",
            "body language",
            "eloquence",
            "empathy",
            "assertiveness",
            "effective communication",
            "mutual understanding"
        ]

        initiative = [
            "proactivity",
            "leadership",
            "autonomy",
            "decision making",
            "responsibility",
            "creativity",
            "innovation",
            "perseverance",
            "strategic vision",
            "risk-taking",
            "entrepreneurial mindset",
            "independence",
            "self-motivation",
            "problem solving",
            "boldness"
        ]

        teamwork = [
            "collaboration",
            "cooperation",
            "empathy",
            "trust",
            "effective communication",
            "flexibility",
            "commitment",
            "mutual support",
            "respect",
            "diversity",
            "synergy",
            "harmony",
            "shared leadership",
            "constructive feedback",
            "conflict management"
        ]

        leadership = [
            "leadership skills",
            "team motivation",
            "strategic vision",
            "inspiration",
            "decision making",
            "delegation",
            "positive influence",
            "responsibility",
            "charisma",
            "results orientation",
            "ethics",
            "communication skills",
            "adaptability",
            "change management",
            "ability to inspire trust"
        ]

        organization = [
            "planning",
            "prioritization",
            "discipline",
            "efficiency",
            "time management",
            "personal organization",
            "meeting deadlines",
            "structuring",
            "focus",
            "resource management",
            "project management",
            "informed decision making",
            "attention to detail",
            "systematization"
        ]

        print(' '.join(comment) + " - " + str(self.verify_polarity(' '.join(comment))))
        
        for word in comment:
            if word == '': continue
            if word in communication:
                self.__soft_skills['Communication'] += self.verify_polarity(' '.join(comment))
            if word in teamwork:
                self.__soft_skills['Teamwork'] += self.verify_polarity(' '.join(comment))
            if word in initiative:
                self.__soft_skills['Initiative'] += self.verify_polarity(' '.join(comment))
            if word in leadership:
                self.__soft_skills['Leadership'] += self.verify_polarity(' '.join(comment))
            if word in organization:
                self.__soft_skills['Organization'] += self.verify_polarity(' '.join(comment))
    
    def verify_hard_skills(self, comment: str) -> None:
        
        programming_languages = [
            'python', 'java', 'javascript', 'c', 'c++', 'c#', 'ruby', 'php', 'swift', 'kotlin', 'typescript', 'go', 'rust', 'perl', 'scala', 'haskell', 
            'object-oriented', 'debugging', 'code performance', 'programming paradigms', 'interpreters', 'compilers', 'ides', 'libraries', 'best practices', 
            'functions', 'inheritance', 'classes', 'objects', 'lists', 'arrays', 'modularity', 'abstraction', 'concurrency', 'memory management', 'error handling', 
            'lambda expressions', 'functional programming', 'parallel computing', 'data structures', 'algorithms', 'event-driven programming'
        ]
        
        software_testing = [
            'unit testing', 'integration testing', 'functional testing', 'test automation', 'regression testing', 'load testing', 'performance testing', 'exploratory testing', 
            'test cases', 'test plans', 'test strategies', 'test environments', 'test coverage', 'defect tracking', 'continuous integration', 'mocking', 'test automation frameworks', 
            'test execution', 'test reporting', 'test management tools', 'load balancer testing', 'endpoint security testing', 'data validation testing', 'mock objects'
        ]

        web_development = [
            'html', 'css', 'javascript', 'react', 'angular', 'vue.js', 'node.js', 'python', 'ruby', 'php', 'apis', 'single-page applications', 'spa', 'user interface',
            'responsive design',  'frontend', 'backend', 'web servers', 'RESTful APIs', 'microservices', 'state management', 'web security', 'performance optimization',
            'frontend frameworks', 'backend frameworks', 'cloud computing', 'containerization', 'web sockets', 'content delivery networks', 'cdns', 'cors',
            'user authentication', 'cross-origin resource sharing'
        ]

        desktop_development = [
            'gui', '.net', 'javafx', 'electron', 'cross-platform development', 'windows forms', 'cocoa', 'qt framework', 'native development', 'windows',
            'user interface', 'cross-platform compatibility', 'system integration', 'native libraries', 'desktop applications', 'UI/UX design', 'desktop security',
            'system resources management', 'multi-threading', 'desktop GUI frameworks', 'application lifecycle management', 'desktop security measures', 'macos',
            'remote access', 'user permissions management', 'linux'
        ]

        databases = [
            'sql', 'nosql', 'mysql', 'postgresql', 'mongodb', 'oracle database', 'data modeling', 'indexing', 'transactions', 'query optimization', 
            'data replication', 'clustering', 'backups', 'cloud storage', 'database administration', 'data warehousing', 'data integrity', 'data consistency', 
            'database scaling', 'data migration', 'data recovery', 'data encryption', 'data validation', 'database schemas', 'data indexing', 'database normalization', 
            'data partitioning', 'database triggers', 'data replication strategies', 'query tuning', 'data archival', 'database performance monitoring'
        ]

        logic_programming = [
            'prolog', 'datalog', 'constraint logic programming', 'automated reasoning', 'declarative programming', 'knowledge representation', 'clp',
            'inference engines', 'logical reasoning',  'knowledge bases', 'logical constraints', 'rule-based systems', 'temporal logic', 'formal logic', 
            'inference mechanisms', 'logic programming languages', 'constraint satisfaction', 'logic solvers', 'logic-based reasoning', 'rule engines', 
            'temporal databases', 'formal verification'
        ]

        application_security = [
            'vulnerabilities', 'penetration testing', 'owasp top 10', 'encryption', 'authentication', 'authorization', 'secure coding practices', 'security audits',
            'threat modeling', 'security frameworks', 'secure coding guidelines', 'vulnerability management', 'incident response', 'security protocols', 'sdlc',
            'penetration testing tools', 'security compliance', 'firewall configuration', 'incident response planning', 'data masking techniques', 'secure practices'
        ]

        machine_learning = [
            'supervised learning', 'unsupervised learning', 'deep learning', 'neural networks', 'tensorflow', 'pytorch', 'reinforcement learning', 'recommender systems',
            'natural language processing', 'feature engineering', 'model evaluation', 'data preprocessing', 'hyperparameter tuning', 'model deployment', 'model interpretation',
            'feature selection', 'ensemble methods', 'cross-validation', 'anomaly detection', 'bias-variance tradeoff', 'gradient boosting', 'time series forecasting'
        ]

        iot = [
            'sensors', 'actuators', 'embedded systems', 'mqtt', 'coap', 'http', 'edge computing', 'wireless communication', 'bluetooth', 'zigbee', 'lora',
            'iot platforms', 'iot security','communication protocols', 'telemetry', 'home automation', 'connected devices', 'iot', 'environmental sensors', 
            'remote control', 'physical security', 'system integration', 'sensors integration', 'iot device management', 'edge analytics',
            'data visualization', 'onnectivity standards', 'firmware updates', 'data aggregation', 'interoperability'
        ]

        keyword_lists = {
            'programming_languages': programming_languages,
            'software_testing': software_testing,
            'web_development': web_development,
            'desktop_development': desktop_development,
            'databases': databases,
            'logic_programming': logic_programming,
            'application_security': application_security,
            'machine_learning': machine_learning,
            'iot': iot
        }

        # index = 0
        # for word in comment:
        #     for skill_key, skill_list in keyword_lists.items():
        #         index += 1
        #         if word in skill_list:
        #             self.__hard_skills[index]['value'] += self.verify_polarity(' '.join(comment))
                    

        for word in comment:
            if word in programming_languages: self.__hard_skills[0]['value'] += self.verify_polarity(' '.join(comment))
            if word in software_testing: self.__hard_skills[1]['value'] += self.verify_polarity(' '.join(comment))
            if word in web_development: self.__hard_skills[2]['value'] += self.verify_polarity(' '.join(comment))
            if word in desktop_development: self.__hard_skills[3]['value'] += self.verify_polarity(' '.join(comment))
            if word in databases: self.__hard_skills[4]['value'] += self.verify_polarity(' '.join(comment))
            if word in logic_programming: self.__hard_skills[5]['value'] += self.verify_polarity(' '.join(comment))
            if word in application_security: self.__hard_skills[6]['value'] += self.verify_polarity(' '.join(comment))
            if word in machine_learning: self.__hard_skills[7]['value'] += self.verify_polarity(' '.join(comment))
            if word in iot: self.__hard_skills[8]['value'] += self.verify_polarity(' '.join(comment))
        
    

    
    def verify_polarity(self, comment):
        blob = TextBlob(comment)
        polarity = blob.sentiment.polarity
        return polarity
        
            
        
      
        
