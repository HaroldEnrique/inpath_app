# coding=utf-8
# services/main/project/api/encuesta.pyF

from flask_restful import Resource, Api
from flask import Blueprint, request
from sqlalchemy import exc
from project import db
from project.api.model_encuesta import TipoPregunta, Pregunta
from project.api.model_encuesta import TipoEncuesta, Encuesta, Opcion

encuesta_blueprint = Blueprint('encuesta', __name__)
api = Api(encuesta_blueprint)


class EncuestaPing(Resource):
    def get(self):
        return {
            'status': 'success_encuesta',
            'message': 'pong!'
        }


class EncuestaList(Resource):

    def get(self):
        """Listar Config Test"""

        q = db.session.query(TipoEncuesta, Encuesta, TipoPregunta,
                             Pregunta, Opcion).filter(
                    TipoEncuesta.id == Encuesta.id_tipo_encuesta,
                    Encuesta.id == Pregunta.id_test,
                    TipoPregunta.id == Pregunta.id_tipo_pregunta,
                    Pregunta.id == Opcion.id_pregunta).all()

        lista = []
        for i in q:
            dict_tipo_encuesta = i[0].to_json()
            dict_encuesta = i[1].to_json()
            dict_tipo_pregunta = i[2].to_json()
            dict_pregunta = i[3].to_json()
            dict_opcion = i[4].to_json()

            dict_pregunta["opciones"] = dict_opcion
            dict_pregunta["tipo_pregunta"] = dict_tipo_pregunta
            dict_encuesta["pregunta"] = dict_pregunta
            dict_tipo_encuesta["encuesta"] = dict_encuesta

            lista.append(dict_tipo_encuesta)

        response_object = {
            'status': 'success',
            'data': lista
        }
        return response_object, 200

    def post(self):
        post_data = request.get_json()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        if not post_data:
            return response_object, 400

        id_test = post_data.get('id_test')
        id_tipo_test = post_data.get('id_tipo_test')
        nombre_test = post_data.get('nombre_test')
        descripcion_test = post_data.get('descripcion_test')
        created_by = post_data.get('created_by')
        preguntas = post_data.get('preguntas')

        try:
            if id_test == "0":
                encuesta = Encuesta(
                    nombre=nombre_test,
                    descripcion=descripcion_test,
                    estado=1,
                    id_tipo_encuesta=id_tipo_test,
                    created_by=created_by
                )
                db.session.add(encuesta)
                db.session.flush()
                encuesta_id = encuesta.id

                for i in preguntas:
                    nom_preg = i['pregunta']
                    tipo_pregunta = i['tipo_pregunta']
                    tamanho = i['tamanho']
                    opciones = i['opciones']

                    pregunta = Pregunta(
                        pregunta=nom_preg,
                        tamanho=tamanho,
                        id_tipo_pregunta=tipo_pregunta,
                        id_test=encuesta_id,
                        created_by=created_by
                    )
                    db.session.add(pregunta)
                    db.session.flush()
                    pregunta_id = pregunta.id
                    for j in opciones:
                        texto = j
                        opcion = Opcion(
                            texto=texto,
                            id_pregunta=pregunta_id,
                            created_by=created_by
                        )
                        db.session.add(opcion)
                        db.session.flush()
                db.session.commit()
                response_object['status'] = 'success'
                response_object['message'] = 'el test' f'{nombre_test} fue\
                    agregado!'
            else:
                # test = Encuesta.query.filter_by(id=int(id_test)).first()
                response_object['status'] = 'success'
                response_object['message'] = 'el test' f'{nombre_test} fue\
                    actualizado!'

            return response_object, 201
        except exc.IntegrityError:
            db.session.rollback()
            return response_object, 400


api.add_resource(EncuestaList, '/encuesta')
