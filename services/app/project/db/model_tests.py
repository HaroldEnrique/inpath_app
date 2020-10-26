# coding=utf-8
# services/app/project/db/model_tests.py

from sqlalchemy.sql import func
from project import db
from .entity import Entity
from .model_users import Usuario


class Test(db.Model, Entity):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(255), nullable=False)
    fecha_mod = db.Column(db.String(255), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey(Usuario.__table__.c['id']))
    # created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, nombre, descripcion, estado, fecha_mod, id_usuario, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.fecha_mod = fecha_mod
        self.id_usuario = id_usuario
    
    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "estado": self.estado,
            "fecha_mod": self.fecha_mod,
            "id_usuario": self.id_usuario
        }


class TipoPregunta(db.Model, Entity):
    __tablename__ = 'tipo_pregunta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    tamano = db.Column(db.String(255), nullable=False)

    def __init__(self, nombre, tamano, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.tamano = tamano
    
    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tamano": self.tamano
        }


class Pregunta(db.Model, Entity):
    __tablename__ = 'pregunta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pregunta = db.Column(db.String(255), nullable=False)
    tamano = db.Column(db.String(255), nullable=False)
    id_tipo_pregunta = db.Column(db.Integer, db.ForeignKey(TipoPregunta.__table__.c['id']))
    id_test = db.Column(db.Integer, db.ForeignKey(Test.__table__.c['id']))
    # created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, pregunta, tamano, id_tipo_pregunta, id_test, created_by):
        Entity.__init__(self, created_by)
        self.pregunta = pregunta
        self.tamano = tamano
        self.id_tipo_pregunta = id_tipo_pregunta
        self.id_test = id_test
    
    def to_json(self):
        return {
            "id": self.id,
            "pregunta": self.pregunta,
            "tamano": self.tamano,
            "id_tipo_pregunta": self.id_tipo_pregunta,
            "id_test": self.id_test,
        }


class OpcionDetalle(db.Model, Entity):
    __tablename__ = 'opcion_detalle'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.String(255), nullable=False)
    id_pregunta = db.Column(db.Integer, db.ForeignKey(Pregunta.__table__.c['id']))

    def __init__(self, texto, id_pregunta, created_by):
        Entity.__init__(self, created_by)
        self.texto = texto
        self.id_pregunta = id_pregunta
    
    def to_json(self):
        return {
            "id": self.id,
            "texto": self.texto,
            "id_pregunta": self.id_pregunta
        }


class Respuesta(db.Model, Entity):
    __tablename__ = 'respuesta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.String(255), nullable=False)
    id_opcion_detalle = db.Column(db.Integer, db.ForeignKey(OpcionDetalle.__table__.c['id']))
    id_usuario = db.Column(db.Integer, db.ForeignKey(Usuario.__table__.c['id']))

    def __init__(self, texto, id_opcion_detalle, id_usuario, created_by):
        Entity.__init__(self, created_by)
        self.texto = texto
        self.id_opcion_detalle = id_opcion_detalle
        self.id_usuario = id_usuario
    
    def to_json(self):
        return {
            "id": self.id,
            "texto": self.texto,
            "id_opcion_detalle": self.id_opcion_detalle
            "id_usuario": self.id_usuario
        }