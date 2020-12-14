# coding=utf-8
# services/main/project/api/model_perfil.py

from project import db
from .entity import Entity
from project.api.model_encuesta import Encuesta
from project.api.model_usuarios import Usuario


class Carrera(db.Model, Entity):
    __tablename__ = 'carrera'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)

    def __init__(self, nombre, descripcion, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.descripcion = descripcion

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion
        }


class TipoPerfil(db.Model, Entity):
    __tablename__ = 'tipo_perfil'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
    id_tipo_encuesta = db.Column(
        db.Integer, db.ForeignKey(Encuesta.__table__.c['id']))

    def __init__(self, nombre, descripcion, id_tipo_encuesta, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_tipo_encuesta = id_tipo_encuesta

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "id_tipo_encuesta": self.id_tipo_encuesta
        }


class PerfilCarrera(db.Model, Entity):

    __tablename__ = 'perfil_carrera'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_carrera = db.Column(
        db.Integer, db.ForeignKey(Carrera.__table__.c['id']))
    id_tipo_perfil = db.Column(
        db.Integer, db.ForeignKey(TipoPerfil.__table__.c['id']))

    def __init__(self, id_carrera, id_tipo_perfil, created_by):
        Entity.__init__(self, created_by)
        self.id_carrera = id_carrera
        self.id_tipo_perfil = id_tipo_perfil

    def to_json(self):
        return {
            "id": self.id,
            "id_carrera": self.id_carrera,
            "id_tipo_perfil": self.id_tipo_perfil,
        }


class ResultadoDetalle(db.Model, Entity):

    __tablename__ = 'resultado_detalle'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Integer, nullable=False)
    etiqueta_ia = db.Column(db.String(255), nullable=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey(
        Usuario.__table__.c['id']))
    # id_tipo_perfil = db.Column(db.Integer, nullable=True)
    id_tipo_perfil = db.Column(db.Integer, db.ForeignKey(
        TipoPerfil.__table__.c['id']))
    id_encuesta = db.Column(db.Integer, db.ForeignKey(
        Encuesta.__table__.c['id']))

    def __init__(self, valor, estado, etiqueta_ia, id_usuario,
                 id_tipo_perfil, id_encuesta, created_by):
        Entity.__init__(self, created_by)
        self.valor = valor
        self.estado = estado
        self.etiqueta_ia = etiqueta_ia
        self.id_usuario = id_usuario
        self.id_tipo_perfil = id_tipo_perfil
        self.id_encuesta = id_encuesta

    def to_json(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "estado": self.estado,
            "etiqueta_ia": self.etiqueta_ia,
            "id_usuario": self.id_usuario,
            "id_tipo_perfil": self.id_tipo_perfil,
            "id_encuesta": self.id_encuesta
        }
