from flask import jsonify, Blueprint, request

#jsonify: tranformas as respostas em json para o usuário
#Blueprint: ajuda a dar um nome bacana para a rotas para saber melhor a que ela se refere

routes_bp = Blueprint("routes", __name__)

# Importação de Controllers

from src.controllers.students_avaliation_graph import StudentsAvaliationGraph
from src.controllers.disciplines_competences import DisciplinesCompetencesGraph

# Importação de Repositorios

from src.models.repositories.student_avaliation_repository import StudentAvaliationRepository
from src.models.repositories.profiles_repository import ProfileRepository
from src.models.repositories.courses_repository import CoursesRepository
from src.models.repositories.disciplines_repository import DisciplinesRepository
from src.models.repositories.competences_repository import CompetencesRepository
from src.models.repositories.student_competences_repository import StudentCompetencesRepository

# Importação de gerente de conexões

from src.models.settings.db_connection_handler import db_connection_handler


@routes_bp.route("/students-avaliation/<ProfileId>", methods=["GET"])
def students_avaliation_hard_and_soft_skills(ProfileId):
    conn = db_connection_handler.get_connection()
    students_avaliation_repository = StudentAvaliationRepository(conn)
    profile_repository = ProfileRepository(conn)
    courses_repository = CoursesRepository(conn)

    controller = StudentsAvaliationGraph(students_avaliation_repository, profile_repository, courses_repository)
    response =  controller.find_avaliations(ProfileId)

    return jsonify(response["body"]), response["status_code"]

@routes_bp.route("/disciplines-competences/<ProfileId>", methods=["GET"])
def disciplines_competences(ProfileId):
    conn = db_connection_handler.get_connection()
    profile_repository = ProfileRepository(conn)
    disciplines_repository =  DisciplinesRepository(conn)
    competences_repository = CompetencesRepository(conn)
    courses_repository = CoursesRepository(conn)
    student_competences_repository = StudentCompetencesRepository(conn)

    controller = DisciplinesCompetencesGraph(profile_repository, disciplines_repository, competences_repository, courses_repository, student_competences_repository)
    response =  controller.find_disciplines_competences(ProfileId)

    return jsonify(response["body"]), response["status_code"]

