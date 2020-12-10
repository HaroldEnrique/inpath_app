# coding=utf-8
# services/main/project/api/model_campana.py

from project import db
from .entity import Entity

class Carrera(db.Model, Entity):
    __tablename__ = 'carrera'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)

    def __init__(self, nombre, descripcion, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.descripcion = descripcion

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "created_at": self.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%dT%H:%M:%S'),
            "last_updated_by": self.last_updated_by
        }


class TipoPerfil(db.Model, Entity):
    __tablename__ = 'tipo_perfil'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)

    def __init__(self, nombre, descripcion, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.descripcion = descripcion

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "created_at": self.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%dT%H:%M:%S'),
            "last_updated_by": self.last_updated_by
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
