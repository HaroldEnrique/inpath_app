# coding=utf-8
# services/main/project/api/encuesta.pyF

from flask_restful import Resource, Api
from flask import Blueprint, request
from sqlalchemy import exc
from project import db
from project.api.model_encuesta import TipoPregunta, Pregunta, Resultado
from project.api.model_encuesta import TipoEncuesta, Encuesta, Opcion, Respuesta

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

class temp_a:  
    def __init__(self, id_perfil, valor, estado):  
        self.id_perfil = id_perfil  
        self.valor = valor
        self.estado = estado 


class RespuestaList(Resource):

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
        
        id_user = post_data.get('id_user')
        id_test = post_data.get('id_test')
        etiqueta_ia = post_data.get('etiqueta_ia')
        opciones = post_data.get('ids_opciones')

        try:
            array_temp = [] 

            for i in opciones:
                opcion = Opcion.query.filter_by(id_opcion=i).first() 
                id_pregunta = opcion.id_pregunta
                texto = opcion.texto 
                valor = opcion.valor
                respuesta = Respuesta(
                    id_opcion=texto,
                    id_usuario=id_user
                )                 
                db.session.add(respuesta)
                db.session.flush()
                pregunta = Pregunta.query.filter_by(id_pregunta=id_pregunta).first() 
                id_perfil = pregunta['id_tipo_perfil']
                
                if array_temp: 
                    for j in array_temp:
                        if(j['id_perfil']== id_perfil):
                            j['valor']= j['valor'].astype(str).astype(int) +valor
                        else:
                            temporal = temp_a(
                                id_perfil=id_perfil,
                                valor=valor,
                                estado = "0"
                            ) 
                            array_temp.append(temporal)
                else:
                    temporal = temp_a(
                        id_perfil=id_perfil,
                        valor=valor,
                        estado="0"
                    ) 
                    array_temp.append(temporal)

            
            i = 0
            while i<len(array_temp):
                j = 0
                result = 0
                while j <len(array_temp):
                    if array_temp[i].valor >= array_temp[j].valor:
                        result=result+1
                    
                    j=j+1
                
                if result == len(array_temp):
                    array_temp[i].estado = "1"

                i=i+1
                
            for k in array_temp:
                resultado = Resultado(
                    valor = k['valor'] ,
                    estado = k['estado'] , 
                    etiqueta_ia=etiqueta_ia,
                    id_usuario=id_user,
                    id_test=id_test,
                    created_by=id_user
                )
                db.session.add(resultado)
                db.session.flush()

            db.session.commit()
            response_object['status'] = 'success'
            response_object['message'] = 'Las respuestas y resultados se agregaron correctamente'
            return response_object, 201

        except exc.IntegrityError:
            db.session.rollback()
            return response_object, 400


api.add_resource(EncuestaList, '/encuesta')
api.add_resource(RespuestaList, '/encuestaR')