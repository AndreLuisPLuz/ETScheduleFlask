# travel-itinerary
# Aula 1
https://app.rocketseat.com.br/events/nlw-journey/python/aula-01-python

## Banco de dados(SQLlite)
https://dbeaver.io/download/

## User Guide:
https://virtualenv.pypa.io/en/latest/user_guide.html

pip install virtualenv
python -m venv venv 
    Estamos nomeando o venv como "venv"
    Essa pasta venv serve para fazer intalar coisas que seram utilizadas sem necessariamente instalar na maquina, dessa forma deixando menos poluido

.\venv\Scripts\Activate
    trabalhar com diferentes locais de python

## Framework Flask
https://pypi.org/project/Flask/

pip3 install Flask
    como estamos no ambiente virtual venv, quando instalamos, por exemplo o Flask ele na verdade está sendo instaladp dentro da pasta venv 

* Quando criamos uma pasta em python criar um arquino __init__.py que possibilitara a importação e exportação de arquivos (ex de import: from src.main.server.server import app)

Dentro da pasta src/main/server estaram as configurações de servidor

* Para rodar o servidor:
python run.py

Configuro minha pasta .vscode no arquivo settings.json para tornar "invissivel" todos aqueles arquivos que estariam poluindo visualmente meu projeto

pasta models/settings para se conectar com o banco de dados

models/repositories para fazer ações no nosso banco

# pytest:
https://pypi.org/project/pytest/
https://docs.pytest.org/en/latest/

pip3 install pytest

# Rodar os testes unitários:
pytest -s -v src/models/repositories/trips_repository_test.py
pytest -s -v src/models/repositories/emails_to_invite_repository_test.py
pytest -s -v src/models/repositories/links_repository_test.py

# Aula 2
https://app.rocketseat.com.br/events/nlw-journey/python/aula-02-python

Dentro da pasta src/main/server etaram as logicas de processos, como de inserção busca, viagens etc.

# Aula 3
## Framework Resquests
pip3 install requests
https://pypi.org/project/requests/

vamos testar com email ficticios com esse comando:
python create_email.py

depois é só fazer o login com a resposta no site a baixo
https://ethereal.email/
