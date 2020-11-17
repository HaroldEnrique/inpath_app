# coding=utf-8
# services/main/project/api/encuesta.py
import decimal,datetime, json
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

    def get(self):
        """Listar Config Test"""

        q = db.session.query(TipoEncuesta, Encuesta, TipoPregunta, Pregunta, Opcion)\
            .filter(TipoEncuesta.id == Encuesta.id_tipo_encuesta,
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
            
            print(dict_tipo_encuesta)
            lista.append(dict_tipo_encuesta) 

        

        response_object = {
            'status': 'success',
            'data': lista
        }
        return response_object, 200


api.add_resource(EncuestaList, '/encuesta')