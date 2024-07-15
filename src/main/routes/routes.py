from flask import jsonify, Blueprint, request

#jsonify: tranformas as respostas em json para o usuário
#Blueprint: ajuda a dar um nome bacana para a rotas para saber melhor a que ela se refere

routes_bp = Blueprint("routes", __name__)

# Importação de Controllers

from src.controllers.students_avaliation_finder import StudentsAvaliationFinder

# Importação de Repositorios

from src.models.repositories.student_avaliation_repository import StudentAvaliationRepository
from src.models.repositories.profile_repository import ProfileRepository

# Importação de gerente de conexões

from src.models.settings.db_connection_handler import db_connection_handler


@routes_bp.route("/graphs/<ProfileId>", methods=["GET"])
def teste(ProfileId):
    conn = db_connection_handler.get_connection()
    students_avaliation_repository = StudentAvaliationRepository(conn)
    profile_repository = ProfileRepository(conn)

    controller = StudentsAvaliationFinder(students_avaliation_repository, profile_repository)
    response =  controller.find_avaliations(ProfileId)

    return jsonify(response["body"]), response["status_code"]


