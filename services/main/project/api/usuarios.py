# coding=utf-8
# services/main/project/api/usuarios.py

from flask_restful import Resource, Api
from sqlalchemy import exc
from flask import Blueprint, request

from project import db
from project.api.model_usuarios import Persona

usuarios_blueprint = Blueprint('usuarios', __name__)
api = Api(usuarios_blueprint)


class UsuariosPing(Resource):
    def get(self):
        return {
            'status': 'success_usuarios',
            'message': 'pong!'
        }


class PersonasList(Resource):
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
        """Get all persons"""

        response_object = {
            'status': 'success',
            'data': {
                'personas':
                    [persona.to_json() for persona in Persona.query.all()]
            }
        }
        return response_object, 200


class Personas(Resource):
    def get(self, persona_id):
        """Obtenga detalles de un solo usuario."""
        response_object = {
            'status': 'fail',
            'message': 'Persona does not exist'
        }
        try:
            persona = Persona.query.filter_by(id=int(persona_id)).first()
            if not persona:
                return response_object, 404
            else:
                response_object = {
                    'status': 'success',
                    'data': persona.to_json()
                }
                return response_object, 200
        except ValueError:
            return response_object, 404


api.add_resource(UsuariosPing, '/usuarios/ping')
api.add_resource(PersonasList, '/personas')
api.add_resource(Personas, '/personas/<persona_id>')
