# coding=utf-8
# services/main/project/api/model_campana.py

from project import db
from .entity import Entity
from project.api.model_encuesta import Encuesta


class Campana(db.Model, Entity):
    __tablename__ = 'campana'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    lugar = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Integer, nullable=False)
    codigo = db.Column(db.String(255), nullable=False)

    def __init__(self, nombre, lugar, descripcion, fecha, hora,
                 estado, codigo, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.lugar = lugar
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.codigo = codigo

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "lugar": self.lugar,
            "descripcion": self.descripcion,
            "fecha": self.fecha.strftime('%Y-%m-%d'),
            "hora": self.hora,
            "estado": self.estado,
            "codigo": self.codigo,
            "created_at": self.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%dT%H:%M:%S'),
            "last_updated_by": self.last_updated_by
        }


class CampanaTest(db.Model, Entity):

    __tablename__ = 'campana_test'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    estado = db.Column(db.Integer, nullable=False)
    id_campana = db.Column(
        db.Integer, db.ForeignKey(Campana.__table__.c['id']))
    id_test = db.Column(
        db.Integer, db.ForeignKey(Encuesta.__table__.c['id']))

    def __init__(self, estado, id_campana, id_test, created_by):
        Entity.__init__(self, created_by)
        self.estado = estado
        self.id_campana = id_campana
        self.id_test = id_test

    def to_json(self):
        return {
            "id": self.id,
            "estado": self.estado,
            "id_campana": self.id_campana,
            "id_test": self.id_test
        }
