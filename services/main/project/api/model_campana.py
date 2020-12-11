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
    modo = db.Column(db.String(255), nullable=True)
    complemento = db.Column(db.String(255), nullable=True)

    def __init__(self, nombre, lugar, descripcion, fecha, hora,
                 estado, codigo, modo, complemento, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.lugar = lugar
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.codigo = codigo
        self.modo = modo
        self.complemento = complemento

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
            "modo": self.modo,
            "complemento": self.complemento
        }


class CampanaEncuesta(db.Model, Entity):

    __tablename__ = 'campana_encuesta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    estado = db.Column(db.Integer, nullable=False)
    id_campana = db.Column(
        db.Integer, db.ForeignKey(Campana.__table__.c['id']))
    id_encuesta = db.Column(
        db.Integer, db.ForeignKey(Encuesta.__table__.c['id']))

    def __init__(self, estado, id_campana, id_encuesta, created_by):
        Entity.__init__(self, created_by)
        self.estado = estado
        self.id_campana = id_campana
        self.id_encuesta = id_encuesta

    def to_json(self):
        return {
            "id": self.id,
            "estado": self.estado,
            "id_campana": self.id_campana,
            "id_encuesta": self.id_encuesta
        }
