use etschedule


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
    (1, 1, 'student', 'The development of soft skills is equally crucial for students academic and professional success. These interpersonal skills complement technical proficiency by fostering effective communication, teamwork, leadership, adaptability, problem solving, and time management. Soft skills enable individuals to collaborate seamlessly in diverse teams, navigate challenges with resilience, and adapt to dynamic environments. Creativity and emotional intelligence empower individuals to innovate and empathize, fostering a supportive and productive workplace culture.'),
    (2, 1, 'student', 'Critical thinking and decision-making skills enable informed judgments and strategic planning. Additionally, conflict resolution, collaboration, empathy, resilience, flexibility, networking, negotiation, presentation skills, listening, and initiative are integral for building strong professional relationships and achieving organizational goals. Developing both hard and soft skills equips individuals with a well-rounded skill set essential for thriving in todays competitive academic and professional landscape.'),
    (3, NULL, 'instructor', NULL),
	(4, NULL, 'instructor', NULL),
	(5, NULL,  'administrator', NULL);


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


INSERT INTO student_competences (competence_id, student_id, degree)
VALUES
	-- Student 1
    (1, 1, 'inapt'),-- React
	(2, 1, 'apt'),

	(3, 1, 'inapt'), -- Java
	(4, 1, 'inapt'),

	(5, 1, 'inapt'),-- Python
	(6, 1, 'progress'),

	(7, 1, 'apt'),-- SQL
	(8, 1, 'apt'),

	-- Student 2
    (1, 2, 'inapt'),-- React
	(2, 2, 'inapt'),

	(3, 2, 'inapt'),-- Java
	(4, 2, 'apt'),

	(5, 2, 'apt'), -- Python
	(6, 2, 'apt'),
	
	(7, 2, 'progress'),-- SQL
	(8, 2, 'progress');


INSERT INTO students_avaliation (discipline_id, student_id, comment) 
VALUES
    -- Habilidades Interpessoais e de Comunicação
    (1, 1, 'Demonstrates strong interpersonal skills and effective communication, contributing positively to team projects and client interactions.'),
    (1, 2, 'Exhibits leadership qualities and excellent collaboration skills, fostering a cohesive team environment during project execution.'),

    -- Habilidades de Pensamento Crítico e Resolução de Problemas
    (2, 1, 'Applies critical thinking and problem-solving skills to address complex programming challenges, ensuring efficient and scalable solutions.'),
    (2, 2, 'Demonstrates strategic thinking and analytical prowess in Java application development, focusing on optimizing performance and code quality.'),

    -- Habilidades de Autogestão e Eficiência Pessoal
    (3, 1, 'Manages time effectively and demonstrates resilience in meeting project deadlines and overcoming obstacles in Python web development tasks.'),
    (3, 2, 'Shows initiative and adaptability in handling diverse scripting and backend development tasks using Python and its libraries.'),

    -- Habilidades Criativas e Inovadoras
    (4, 1, 'Applies creativity and problem sensitivity to design efficient database schemas and optimize SQL queries for data manipulation and analysis.'),
    (4, 2, 'Incorporates imaginative solutions and artistic skills in database management, ensuring data integrity and performance optimization.');




	-- Select all rows from users table
SELECT * FROM users;

-- Select all rows from groups table
SELECT * FROM groups;

-- Select all rows from profiles table
SELECT * FROM profiles;


-- Select all rows from courses table
SELECT * FROM courses;

-- Select all rows from disciplines table
SELECT * FROM disciplines;

-- Select all rows from events table
SELECT * FROM [events];

-- Select all rows from instructor_skills table
SELECT * FROM instructor_skills;

-- Select all rows from competences table
SELECT * FROM competences;

-- Select all rows from student_competences table
SELECT * FROM student_competences;

-- Select all rows from students_avaliation table
SELECT * FROM students_avaliation;