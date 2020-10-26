# coding=utf-8
# services/app/project/db/model_campanas.py

from sqlalchemy.sql import func
from project import db
from .entity import Entity
from .model_users import Usuario
from .model_tests import Test

class Campana(db.Model, Entity):
    __tablename__ = 'campana'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    lugar = db.Column(db.String(255), nullable=False)
    fecha_hora = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(255), nullable=False)
    codigo = db.Column(db.String(255), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey(Usuario.__table__.c['id']))

    def __init__(self, nombre, descripcion, lugar, fecha_hora, estado, codigo, id_usuario, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.descripcion = descripcion
        self.lugar = lugar
        self.fecha_hora = fecha_hora
        self.estado = estado
        self.codigo = codigo
        self.id_usuario = id_usuario
        
    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "lugar": self.lugar,
            "fecha_hora": self.fecha_hora,
            "estado": self.estado,
            "codigo": self.codigo,
            "id_usuario": self.id_usuario
        }

class CampanaTest(db.Model, Entity):
    __tablename__ = 'campana_test'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_campana = db.Column(db.Integer, db.ForeignKey(Campana.__table__.c['id']))
    id_test = db.Column(db.Integer, db.ForeignKey(Test.__table__.c['id']))

    def __init__(self, id_campana, id_test, created_by):
        Entity.__init__(self, created_by)
        self.id_campana = id_campana
        self.id_test = id_test
        
    def to_json(self):
        return {
            "id": self.id,
            "id_campana": self.id_campana,
            "id_test": self.id_test
        }