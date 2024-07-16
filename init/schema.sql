create database etschedule

use etschedule

CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username NVARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    full_name NVARCHAR(255) NOT NULL,
    [password] NVARCHAR(255) NOT NULL
);


CREATE TABLE groups (
    id INT IDENTITY(1,1) PRIMARY KEY,
    [name] NVARCHAR(255) NOT NULL,
    begins_at DATE NOT NULL,
    ends_at DATE NOT NULL
);


CREATE TABLE profiles (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT NOT NULL,
    group_id INT NOT NULL,
    [role] NVARCHAR(255) NOT NULL,
    consensus NVARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (group_id) REFERENCES groups(id)
);


CREATE TABLE courses (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    description NVARCHAR(MAX) NOT NULL
);


CREATE TABLE disciplines (
    id INT IDENTITY(1,1) PRIMARY KEY,
    group_id INT NOT NULL,
    instructor_id INT NOT NULL,
    course_id INT NOT NULL,
    semester INT NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups(id),
    FOREIGN KEY (instructor_id) REFERENCES users(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);


CREATE TABLE events (
    id INT IDENTITY(1,1) PRIMARY KEY,
    group_id INT NOT NULL,
    discipline_id INT,
    starts_at DATETIME2 NOT NULL,
    ends_at DATETIME2 NOT NULL,
    description NVARCHAR(MAX) NOT NULL,
    CONSTRAINT FK_events_group_id FOREIGN KEY (group_id) REFERENCES groups(id),
    CONSTRAINT FK_events_discipline_id FOREIGN KEY (discipline_id) REFERENCES disciplines(id)
);


CREATE TABLE instructor_skills (
    id INT IDENTITY(1,1) PRIMARY KEY,
    instructor_id INT NOT NULL,
    subject NVARCHAR(255) NOT NULL,
    value INT NOT NULL,
    CONSTRAINT FK_instructor_skills_instructor_id FOREIGN KEY (instructor_id) REFERENCES users(id)
);


CREATE TABLE competences (
    id INT IDENTITY(1,1) PRIMARY KEY,
    discipline_id INT NOT NULL,
    name NVARCHAR(255) NOT NULL,
    weight FLOAT NOT NULL,
    CONSTRAINT FK_competences_discipline_id FOREIGN KEY (discipline_id) REFERENCES disciplines(id)
);


CREATE TABLE student_competences (
    id INT IDENTITY(1,1) PRIMARY KEY,
    competence_id INT NOT NULL,
    student_id INT NOT NULL,
    degree NVARCHAR(255) NOT NULL,
    CONSTRAINT FK_student_competences_competence_id FOREIGN KEY (competence_id) REFERENCES competences(id),
    CONSTRAINT FK_student_competences_student_id FOREIGN KEY (student_id) REFERENCES users(id)
);


CREATE TABLE students_avaliation (
    id INT IDENTITY(1,1) PRIMARY KEY,
    discipline_id INT NOT NULL,
    student_id INT NOT NULL,
    comment NVARCHAR(MAX) NOT NULL,
    CONSTRAINT FK_students_avaliation_discipline_id FOREIGN KEY (discipline_id) REFERENCES disciplines(id),
    CONSTRAINT FK_students_avaliation_student_id FOREIGN KEY (student_id) REFERENCES users(id)
);



