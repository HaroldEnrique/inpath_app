# coding=utf-8
# services/main/project/api/model_encuesta.py

# from sqlalchemy.sql import func
from project import db
from .entity import Entity


class TipoPregunta(db.Model, Entity):

    __tablename__ = 'tipo_pregunta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(255), nullable=False)

    def __init__(self, tipo, created_by):
        Entity.__init__(self, created_by)
        self.tipo = tipo

    def to_json(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
        }

class Pregunta(db.Model, Entity):

    __tablename__ = 'pregunta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pregunta = db.Column(db.String(255), nullable=False)
    tamanho = db.Column(db.String(255), nullable=False)
    id_tipo_pregunta = db.Column(db.Integer, db.ForeignKey(TipoPregunta.__table__.c['id']))
    id_test = db.Column(db.Integer, db.ForeignKey(Encuesta.__table__.c['id']))

    def __init__(self, pregunta, tamanho,id_tipo_pregunta,id_test, created_by):
        Entity.__init__(self, created_by)
        self.pregunta = pregunta
        self.tamanho = tamanho
        self.id_tipo_pregunta = id_tipo_pregunta
        self.id_test = id_test

    def to_json(self):
        return {
            "id": self.id,
            "pregunta": self.pregunta,
            "tamanho": self.tamanho,
            "id_tipo_pregunta": self.id_tipo_pregunta
            "id_test": self.id_test
        }

class TipoEncuesta(db.Model, Entity):

    __tablename__ = 'encuesta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)

    def __init__(self, nombre,created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

class Encuesta(db.Model, Entity):

    __tablename__ = 'encuesta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Integer, nullable=False)
    id_tipo_encuesta = db.Column(db.Integer, db.ForeignKey(TipoEncuesta.__table__.c['id']))

    def __init__(self, nombre, descripcion, estado,id_tipo_encuesta, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.id_tipo_encuesta = id_tipo_encuesta

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "estado": self.estado
            "id_tipo_encuesta":self.id_tipo_encuesta
        }

class Opcion(db.Model, Entity):

    __tablename__ = 'opcion'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.String(255), nullable=False)
    id_pregunta = db.Column(db.Integer, db.ForeignKey(Pregunta.__table__.c['id']))

    def __init__(self, texto,id_pregunta,created_by):
        Entity.__init__(self, created_by)
        self.texto = texto
        self.id_pregunta = id_pregunta

    def to_json(self):
        return {
            "id": self.id,
            "texto": self.texto,
            "id_pregunta": self.id_pregunta
        }