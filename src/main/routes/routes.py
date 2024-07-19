from flask import jsonify, Blueprint, request
from flask_jwt_extended  import jwt_required

#jsonify: tranformas as respostas em json para o usuário
#Blueprint: ajuda a dar um nome bacana para a rotas para saber melhor a que ela se refere

routes_bp = Blueprint("routes", __name__)

# Importação de Controllers

from src.controllers.hard_soft_skills_graph import HardSoftSkillsGraph
from src.controllers.disciplines_average_graph import DisciplinesAverageGraph
from src.controllers.server_auth import ServerAuth

# Importação de Repositorios

from src.models.repositories.student_avaliation_repository import StudentAvaliationRepository
from src.models.repositories.profiles_repository import ProfileRepository
from src.models.repositories.courses_repository import CoursesRepository
from src.models.repositories.disciplines_repository import DisciplinesRepository
from src.models.repositories.competences_repository import CompetencesRepository
from src.models.repositories.student_competences_repository import StudentCompetencesRepository
from src.models.repositories.users_repository import UsersRepository

# Importação de gerente de conexões

from src.models.settings.db_connection_handler import db_connection_handler


@routes_bp.route("/first_access", methods=["POST"])
def aaaaa():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)

    controller = ServerAuth(users_repository)
    response =  controller.firts_access(request.json)

    return jsonify(response["body"]), response["status_code"]


@routes_bp.route("/login", methods=["POST"])
def bbbbb():
    conn = db_connection_handler.get_connection()
    users_repository = UsersRepository(conn)

    controller = ServerAuth(users_repository)
    response =  controller.login(request.json)

    return jsonify(response["body"]), response["status_code"]


@routes_bp.route("/hard-soft-skills/<ProfileId>", methods=["GET"])
@jwt_required()
def cccccc(ProfileId):
    conn = db_connection_handler.get_connection()
    students_avaliation_repository = StudentAvaliationRepository(conn)
    profile_repository = ProfileRepository(conn)

    controller = HardSoftSkillsGraph(students_avaliation_repository, profile_repository)
    response =  controller.find_avaliations(ProfileId)

    return jsonify(response["body"]), response["status_code"]

@routes_bp.route("/disciplines-average/<ProfileId>", methods=["GET"])
@jwt_required()
def dddddd(ProfileId):
    conn = db_connection_handler.get_connection()
    profile_repository = ProfileRepository(conn)
    disciplines_repository =  DisciplinesRepository(conn)
    competences_repository = CompetencesRepository(conn)
    courses_repository = CoursesRepository(conn)
    student_competences_repository = StudentCompetencesRepository(conn)

    controller = DisciplinesAverageGraph(profile_repository, disciplines_repository, competences_repository, courses_repository, student_competences_repository)
    response =  controller.find_disciplines_competences(ProfileId)

    return jsonify(response["body"]), response["status_code"]

