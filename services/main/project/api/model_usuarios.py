# coding=utf-8
# services/main/project/api/model_usuarios.py

# from sqlalchemy.sql import func
from project import db
from .entity import Entity


class Persona(db.Model, Entity):
    __tablename__ = 'persona'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombres = db.Column(db.String(255), nullable=False)
    ape_paterno = db.Column(db.String(255), nullable=False)
    ape_materno = db.Column(db.String(255), nullable=False)
    tipo_doc = db.Column(db.String(255), nullable=False)
    doc = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    colegio = db.Column(db.String(255), nullable=False)
    celular = db.Column(db.Integer, nullable=False)
    fecha_nac = db.Column(db.Date, nullable=False)
    # created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, nombres, ape_paterno, ape_materno, tipo_doc, doc, correo, colegio, celular, fecha_nac, created_by):
        Entity.__init__(self, created_by)
        self.nombres = nombres
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.tipo_doc = tipo_doc
        self.doc = doc
        self.correo = correo
        self.colegio = colegio
        self.celular = celular
        self.fecha_nac = fecha_nac

    def to_json(self):
        return {
            "id": self.id,
            "nombres": self.nombres,
            "ape_materno": self.ape_materno,
            "ape_paterno": self.ape_paterno,
            "tipo_doc": self.tipo_doc,
            "doc": self.doc,
            "correo": self.correo,
            "colegio": self.colegio,
            "celular": self.celular,
            "fecha_nac": self.fecha_nac.strftime('%Y-%m-%dT%H:%M:%S'),
            "created_at": self.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%dT%H:%M:%S'),
            "last_updated_by": self.last_updated_by
        }


class Usuario(db.Model, Entity):

    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    estado = db.Column(db.Integer, nullable=False)
    id_persona = db.Column(
        db.Integer, db.ForeignKey(Persona.__table__.c['id']))

    def __init__(self, usuario, password, estado, id_persona, created_by):
        Entity.__init__(self, created_by)
        self.usuario = usuario
        self.password = password
        self.estado = estado
        self.id_persona = id_persona

    def to_json(self):
        return {
            "id": self.id,
            "usuario": self.usuario,
            "password": self.password,
            "estado": self.estado,
            "id_persona": self.id_persona
        }


class Rol(db.Model, Entity):

    __tablename__ = 'rol'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.Integer, nullable=False)

    def __init__(self, nombre, descripcion, estado, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "estado": self.estado
        }


class UsuarioRol(db.Model, Entity):

    __tablename__ = 'usuario_rol'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    estado = db.Column(db.Integer, nullable=False)
    id_usuario = db.Column(
        db.Integer, db.ForeignKey(Usuario.__table__.c['id']))
    id_rol = db.Column(db.Integer, db.ForeignKey(Rol.__table__.c['id']))

    def __init__(self, estado, id_usuario, id_rol, created_by):
        Entity.__init__(self, created_by)
        self.estado = estado
        self.id_usuario = id_usuario
        self.id_rol = id_rol

    def to_json(self):
        return {
            "id": self.id,
            "estado": self.estado,
            "id_usuario": self.id_usuario,
            "id_rol": self.id_rol
        }
