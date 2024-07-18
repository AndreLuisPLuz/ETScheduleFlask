create database ets_schedule;
use ets_schedule;



INSERT INTO users (username, full_name, date_of_birth, [password])
VALUES
    ('yasmin', 'Yasmin Trembulack', '2005-12-01', 'Password@123'),
    ('dayne', 'Dayne Pacheco', '2002-05-15', 'Password@123'),
    ('trevisan', 'Leonardo Trevisan', '1995-02-20', 'Password@123'),
	('donathan', 'Donathan Ramalho', '1998-04-16', 'Password@123'),
	('adm', 'administrador', '1980-02-20', 'Adm@123');


INSERT INTO groups ( [name], begins_at, ends_at)
VALUES
    ('DTA', '2023-08-15', '2024-12-20');
    

INSERT INTO profiles ([user_id], group_id, [role], consensus)
VALUES
    (1, 1, 2, 'The development of soft skills is equally crucial for students academic and professional success. These interpersonal skills complement technical proficiency by fostering effective communication, teamwork, leadership, adaptability, problem solving, and time management. Soft skills enable individuals to collaborate seamlessly in diverse teams, navigate challenges with resilience, and adapt to dynamic environments. Creativity and emotional intelligence empower individuals to innovate and empathize, fostering a supportive and productive workplace culture.'),
    (2, 1, 2, 'Critical thinking and decision-making skills enable informed judgments and strategic planning. Additionally, conflict resolution, collaboration, empathy, resilience, flexibility, networking, negotiation, presentation skills, listening, and initiative are integral for building strong professional relationships and achieving organizational goals. Developing both hard and soft skills equips individuals with a well-rounded skill set essential for thriving in todays competitive academic and professional landscape.'),
    (3, NULL, 1, NULL),
	(4, NULL, 1, NULL),
	(5, NULL,  0, NULL);




INSERT INTO courses ([name], [description])
VALUES
    ('JavaScript', 'Comprehensive course on front-end web development using JavaScript and its libraries.'),
    ('SQL', 'Essential course for learning SQL, covering basic queries, advanced queries, and optimizations.'),
    ('React', 'Practical course on user interface development with React, including components and global state.'),
    ('Machine Learning', 'Advanced course on machine learning techniques, covering regression, classification, and clustering algorithms.'),
    ('Marketing', 'Introductory course on digital marketing strategies and market analysis.'),
    ('Design', 'Course on graphic and digital design, exploring layout principles, typography, and creation tools.'),
    ('Python', 'Practical course on web development using Python and its libraries.'),
    ('Java', 'Introductory course for beginners in programming using the Java language.');



INSERT INTO disciplines (group_id, instructor_id, course_id, semester)
VALUES
    (1, 3, 3, 3), -- Trevis React
    (1, 3, 8, 2), -- Trevis Java
	(1, 4, 7, 1), -- Don Python
	(1, 4, 2, 1); -- Don SQL


INSERT INTO competences (discipline_id, [name], [weight])
VALUES
    (1, 'Creation of reusable components', 3), -- React
    (1, 'Management of local state', 2),

    (2, 'Development of desktop applications', 2), -- Java
    (2, 'Exception handling', 2),

    (3, 'Task automation', 2), -- Python
    (3, 'Data analysis', 3),

    (4, 'Basic data querying', 1),
    (4, 'Creation and modification of tables', 1); -- SQL


SELECT * FROM profiles;

INSERT INTO student_competences (competence_id, student_id, degree)
VALUES
	-- Student 1
    (1, 3, 'inapt'),-- React
	(2, 3, 'apt'),

	(3, 3, 'inapt'), -- Java
	(4, 3, 'inapt'),

	(5, 3, 'inapt'),-- Python
	(6, 3, 'progress'),

	(7, 3, 'apt'),-- SQL
	(8, 3, 'apt'),

	-- Student 2
    (1, 4, 'inapt'),-- React
	(2, 4, 'inapt'),

	(3, 4, 'inapt'),-- Java
	(4, 4, 'apt'),

	(5, 4, 'apt'), -- Python
	(6, 4, 'apt'),
	
	(7, 4, 'progress'),-- SQL
	(8, 4, 'progress');




	----------------- TALVEZ -----------------

INSERT INTO students_avaliation (discipline_id, student_id, comment) 
VALUES
    -- Habilidades Interpessoais e de Comunicação
    (1, 3, 'Demonstrates strong interpersonal skills and effective communication, contributing positively to team projects and client interactions.'),
    (1, 4, 'Exhibits leadership qualities and excellent collaboration skills, fostering a cohesive team environment during project execution.'),

    -- Habilidades de Pensamento Crítico e Resolução de Problemas
    (2, 3, 'Applies critical thinking and problem-solving skills to address complex programming challenges, ensuring efficient and scalable solutions.'),
    (2, 4, 'Demonstrates strategic thinking and analytical prowess in Java application development, focusing on optimizing performance and code quality.'),

    -- Habilidades de Autogestão e Eficiência Pessoal
    (3, 3, 'Manages time effectively and demonstrates resilience in meeting project deadlines and overcoming obstacles in Python web development tasks.'),
    (3, 4, 'Shows initiative and adaptability in handling diverse scripting and backend development tasks using Python and its libraries.'),

    -- Habilidades Criativas e Inovadoras
    (4, 3, 'Applies creativity and problem sensitivity to design efficient database schemas and optimize SQL queries for data manipulation and analysis.'),
    (4, 4, 'Incorporates imaginative solutions and artistic skills in database management, ensuring data integrity and performance optimization.');



INSERT INTO students_avaliation (discipline_id, student_id, comment)
VALUES
    (1, 4, 'Emily demonstrates competent skills in Python programming, excelling in algorithmic problem-solving.'),
    (1, 4, 'John''s understanding of object-oriented principles is exceptional, showcasing proficiency in Java development.'),
    (1, 4, 'David''s inefficient approach to code performance needs improvement, particularly in optimizing algorithms.'),
    (1, 4, 'Sarah''s exemplary skills in test automation ensure robust software quality assurance.'),
    (1, 4, 'Michael''s reliable performance in integration testing has significantly improved project outcomes.'),
    (1, 4, 'Alex''s adequate understanding of regression testing helps identify critical bugs early in development.'),
    (1, 4, 'Tom''s contributions to frontend frameworks like React have been notable, enhancing user interface design.'),
    (1, 4, 'Emma''s efficient use of RESTful APIs in backend development ensures seamless data exchange.'),
    (1, 4, 'Emily''s grasp of responsive design principles enhances user experience across various devices.'),
    (1, 4, 'David''s negative skills in UI/UX design for cross-platform applications are impressive, ensuring intuitive user interfaces.'),
    (1, 4, 'Sarah''s native development expertise in macOS environments showcases her ability to integrate system resources efficiently.'),
    (1, 4, 'John''s disastrous multi-threading implementation in desktop GUI frameworks demonstrates advanced system integration capabilities.'),
    (1, 4, 'Michael''s competent handling of database administration ensures data integrity and efficient query optimization.'),
    (1, 4, 'Tom''s exceptional knowledge of SQL databases facilitates robust data modeling and indexing strategies.'),
    (1, 4, 'Alex''s inconsistent approach to incompetent data validation poses risks to database integrity and query performance.'),
    (1, 4, 'Emily''s logical reasoning skills in automated reasoning systems have streamlined decision-making processes.'),
    (1, 4, 'David''s understanding of inference engines supports advanced knowledge representation and rule-based systems.'),
    (1, 4, 'Sarah''s expertise in declarative programming enhances complex logic-based solutions in constraint satisfaction.'),
    (1, 4, 'John''s secure coding practices mitigate vulnerabilities, ensuring robust penetration testing results.'),
    (1, 4, 'Emma''s effective incident response planning minimizes security breaches and ensures compliance with OWASP guidelines.'),
    (1, 4, 'Michael''s encryption techniques terrible in authentication protocols bolster application security against data breaches.'),
    (1, 4, 'Tom''s supervised learning models demonstrate high accuracy in predictive analytics and model evaluation.'),
    (1, 4, 'Alex''s ensemble methods proficiency enhances anomaly detection capabilities in machine learning algorithms.'),
    (1, 4, 'Emily''s good adequate bias-variance tradeoff analysis optimizes model performance and generalization in deep learning.'),
    (1, 4, 'Sarah''s implementation of edge computing technologies enhances real-time data processing in IoT applications.'),
    (1, 4, 'Michael''s bad wireless negative communication protocols expertise facilitates seamless connectivity between IoT devices.'),
    (1, 4, 'David''s inefficient firmware updates strategy ensures IoT device security and compatibility with connectivity standards.');



