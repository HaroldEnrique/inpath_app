# coding=utf-8
# services/main/project/api/encuesta.py

from flask_restful import Resource, Api
from sqlalchemy import exc
from flask import Blueprint, request

from project import db
from project.api.model_encuesta import TipoPregunta, Pregunta, TipoEncuesta, Encuesta, Opcion

encuesta_blueprint = Blueprint('encuesta', __name__)
api = Api(encuesta_blueprint)

class EncuestaPing(Resource):
    def get(self):
        return {
            'status': 'success_encuesta',
            'message': 'pong!'
        }

class EncuestaList(Resource):
    def post(self):
        post_data = request.get_json()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        if not post_data:
            return response_object, 400

        nombres = post_data.get('nombres')
        ape_paterno = post_data.get('ape_paterno')
        ape_materno = post_data.get('ape_materno')
        tipo_doc = post_data.get('tipo_doc')
        doc = post_data.get('doc')
        correo = post_data.get('correo')
        colegio = post_data.get('colegio')
        celular = post_data.get('celular')
        fecha_nac = post_data.get('fecha_nac')
        created_by = post_data.get('created_by')

        try:
            person = Persona.query.filter_by(correo=correo).first()
            if not person:
                db.session.add(Persona(
                    nombres=nombres,
                    ape_paterno=ape_paterno,
                    ape_materno=ape_materno,
                    tipo_doc=tipo_doc,
                    doc=doc,
                    correo=correo,
                    colegio=colegio,
                    celular=celular,
                    fecha_nac=fecha_nac,
                    created_by=created_by
                ))
                db.session.commit()
                response_object['status'] = 'success'
                response_object['message'] = f'{correo} was added!'
                return response_object, 201
            else:
                response_object['message'] = 'Sorry. Email already exists.'
                return response_object, 400
        except exc.IntegrityError:
            db.session.rollback()
            return response_object, 400

    def get(self):
        """Listar Config Test"""

        response_object = {
            'status': 'success',
            'data': {
                [TipoEncuesta.to_json() for tipo_encuesta in TipoEncuesta.query.all()]
            }
        }
        return response_object, 200