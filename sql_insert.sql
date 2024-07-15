use etschedule

-- Usuários
INSERT INTO Users (id, username, date_of_birth, fullname, [password])
VALUES (1, 'joao_silva', '1990-05-15', 'João Silva', 'senha123');

INSERT INTO Users (id, username, date_of_birth, fullname, [password])
VALUES (2, 'maria_pereira', '1992-08-20', 'Maria Pereira', 'abc456');

INSERT INTO Users (id, username, date_of_birth, fullname, [password])
VALUES (3, 'carlos_rodrigues', '1988-04-10', 'Carlos Rodrigues', 'qwerty789');

INSERT INTO Users (id, username, date_of_birth, fullname, [password])
VALUES (4, 'ana_santos', '1991-11-25', 'Ana Santos', 'pass123');

INSERT INTO Users (id, username, date_of_birth, fullname, [password])
VALUES (5, 'pedro_almeida', '1993-06-30', 'Pedro Almeida', 'secure789');


-- Perfis
INSERT INTO Profiles (id, [user_id], [role], consensus)
VALUES (1, 1, 'instructor', 'Professor de Matemática');

INSERT INTO Profiles (id, [user_id], [role], consensus)
VALUES (2, 2, 'student', NULL);

INSERT INTO Profiles (id, [user_id], [role], consensus)
VALUES (3, 3, 'student', NULL);

INSERT INTO Profiles (id, [user_id], [role], consensus)
VALUES (4, 4, 'instructor', 'Professora de História');

INSERT INTO Profiles (id, [user_id], [role], consensus)
VALUES (5, 5, 'student', NULL);


-- Disciplinas
INSERT INTO Disciplines (id, instructor_id)
VALUES (1, 1); -- Disciplina de Matemática, instrutor João Silva

INSERT INTO Disciplines (id, instructor_id)
VALUES (2, 1); -- Outra disciplina de Matemática, mesmo instrutor João Silva

INSERT INTO Disciplines (id, instructor_id)
VALUES (3, 4); -- Disciplina de História, instrutor Ana Santos

INSERT INTO Disciplines (id, instructor_id)
VALUES (4, 4); -- Outra disciplina de História, mesmo instrutor Ana Santos



-- Avaliações (já inseridas anteriormente)
INSERT INTO StudentAvaliation (id, discipline_id, student_id, comment)
VALUES (1, 1, 2, 'O aluno demonstrou excelente dedicação e habilidade na disciplina.');

INSERT INTO StudentAvaliation (id, discipline_id, student_id, comment)
VALUES (2, 1, 3, 'O desempenho do aluno foi satisfatório, mas pode melhorar na participação em sala de aula.');

INSERT INTO StudentAvaliation (id, discipline_id, student_id, comment)
VALUES (3, 2, 2, 'O aluno precisa revisar mais os conceitos básicos para melhorar seu desempenho.');

INSERT INTO StudentAvaliation (id, discipline_id, student_id, comment)
VALUES (4, 2, 4, 'Excelente participação e comprometimento do aluno durante todo o semestre.');

INSERT INTO StudentAvaliation (id, discipline_id, student_id, comment)
VALUES (5, 3, 3, 'O aluno mostrou melhora significativa desde o último período. Continuar assim.');

INSERT INTO StudentAvaliation (id, discipline_id, student_id, comment)
VALUES (6, 3, 5, 'Necessário mais esforço por parte do aluno para alcançar os objetivos da disciplina.');

INSERT INTO StudentAvaliation (id, discipline_id, student_id, comment)
VALUES (7, 4, 1, 'Falta de comprometimento do aluno refletiu negativamente no desempenho.');

INSERT INTO StudentAvaliation (id, discipline_id, student_id, comment)
VALUES (8, 4, 3, 'O aluno tem potencial, mas precisa organizar melhor seu tempo de estudo.');

-- Avaliação 9
INSERT INTO StudentAvaliation (id, discipline_id, student_id, comment)
VALUES (9, 1, 2, 'O aluno apresentou um bom entendimento dos conceitos abordados.');

-- Avaliação 10
INSERT INTO StudentAvaliation (id, discipline_id, student_id, comment)
VALUES (10, 3, 2, 'O desempenho do aluno melhorou consideravelmente ao longo do semestre.');


-- Atualizando Maria Pereira (id 2)
UPDATE Profiles
SET consensus = 'Maria Pereira: Demonstrou bom entendimento dos conceitos em Matemática. No entanto, precisa melhorar na participação em História.'
WHERE [user_id] = 2 AND [role] = 'student';

-- Atualizando Carlos Rodrigues (id 3)
UPDATE Profiles
SET consensus = 'Carlos Rodrigues: Apresentou melhora significativa em História. Precisa focar mais na organização do tempo de estudo.'
WHERE [user_id] = 3 AND [role] = 'student';

-- Atualizando Pedro Almeida (id 5)
UPDATE Profiles
SET consensus = 'Pedro Almeida: Mostrou esforço em aprender, mas precisa de mais prática em Matemática.'
WHERE [user_id] = 5 AND [role] = 'student';