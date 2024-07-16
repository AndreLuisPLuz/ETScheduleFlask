-- Inserir os usuários (students e instructor)
-- Não inclua o ID na lista de colunas ao inserir em uma coluna IDENTITY
INSERT INTO users (username, full_name, date_of_birth, [password])
VALUES
    ('student1', 'Student One', '1995-07-01', 'hashed_password_1'),
    ('student2', 'Student Two', '1996-05-15', 'hashed_password_2'),
    ('instructor1', 'Instructor One', '1980-02-20', 'hashed_password_3');

-- Inserir o grupo
-- Não inclua o ID na lista de colunas ao inserir em uma coluna IDENTITY
INSERT INTO groups ([name], begins_at, ends_at)
VALUES ('Group A', '2024-09-01', '2024-12-15');

-- Obter os IDs dos usuários inseridos
DECLARE @student1_id INT, @student2_id INT, @instructor_id INT;
SELECT @student1_id = SCOPE_IDENTITY();  -- ID do student1
SELECT @student2_id = SCOPE_IDENTITY();  -- ID do student2
SELECT @instructor_id = SCOPE_IDENTITY();  -- ID do instructor1

-- Alterar a coluna `consensus` na tabela `profiles` para um tamanho maior, se necessário
ALTER TABLE profiles
ALTER COLUMN consensus NVARCHAR(1000);  -- Ajuste o tamanho conforme necessário


-- Inserir perfis para cada usuário no grupo
INSERT INTO profiles (user_id, group_id, [role], consensus)
VALUES
    (@student1_id, 1, 'Student', 'É fundamental que os alunos desenvolvam tanto soft skills quanto hard skills. Enquanto as hard skills são essenciais para a execução técnica de tarefas, as soft skills são cruciais para a comunicação eficaz, colaboração e adaptação a mudanças. O equilíbrio entre ambas as habilidades é chave para o sucesso tanto acadêmico quanto profissional.'),
    (@student2_id, 1, 'Student', 'O desenvolvimento simultâneo de soft skills e hard skills é crucial para o sucesso acadêmico e profissional dos alunos. Enquanto as hard skills são necessárias para a realização de tarefas específicas, como programação e análise de dados, as soft skills são fundamentais para a interação eficaz em equipe, liderança e resolução de problemas complexos.'),
    (@instructor_id, 1, 'Instructor', NULL);



INSERT INTO courses (name, description)
VALUES
    ('JavaScript', 'Curso abrangente sobre desenvolvimento web front-end utilizando JavaScript e suas bibliotecas.'),
    ('SQL', 'Curso essencial para aprendizado de SQL, abrangendo consultas básicas, avançadas e otimizações.'),
    ('React', 'Curso prático sobre desenvolvimento de interfaces de usuário com React, incluindo componentes e estado global.'),
    ('Machine Learning', 'Curso avançado sobre técnicas de aprendizado de máquina, abordando algoritmos de regressão, classificação e clustering.'),
    ('Marketing', 'Curso introdutório sobre estratégias de marketing digital e análise de mercado.'),
    ('Design', 'Curso de design gráfico e digital, explorando princípios de layout, tipografia e ferramentas de criação.'),
    ('Python', 'Curso prático sobre desenvolvimento web utilizando Python e suas bibliotecas.'),
    ('Java', 'Curso introdutório para iniciantes em programação utilizando a linguagem Java.');
