# coding=utf-8
# services/main/project/api/model_usuarios.py

# from sqlalchemy.sql import func
from project import db
from .entity import Entity


class Departamento(db.Model, Entity):

    __tablename__ = 'departamento'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(128), nullable=False)

    def __init__(self, nombre, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }


class Provincia(db.Model, Entity):

    __tablename__ = 'provincia'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(128), nullable=False)
    id_departamento = db.Column(
        db.Integer, db.ForeignKey(Departamento.__table__.c['id']))

    def __init__(self, nombre, id_departamento, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.id_departamento = id_departamento

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "id_departamento": self.id_departamento
        }


class Distrito(db.Model, Entity):

    __tablename__ = 'distrito'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(128), nullable=False)
    id_provincia = db.Column(
        db.Integer, db.ForeignKey(Provincia.__table__.c['id']))

    def __init__(self, nombre, id_provincia, created_by):
        Entity.__init__(self, created_by)
        self.nombre = nombre
        self.id_provincia = id_provincia

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "id_provincia": self.id_provincia
        }


class Persona(db.Model, Entity):
    __tablename__ = 'persona'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombres = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.String(255), nullable=False)
    tipo_doc = db.Column(db.String(255), nullable=False)
    doc = db.Column(db.Integer, nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    colegio = db.Column(db.String(255), nullable=False)
    celular = db.Column(db.Integer, nullable=False)
    ano_estudio = db.Column(db.Integer, nullable=False)
    id_distrito = db.Column(
        db.Integer, db.ForeignKey(Distrito.__table__.c['id']))
    # created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, nombres, apellidos, tipo_doc, doc, correo,
                 colegio, celular, ano_estudio, id_distrito, created_by):
        Entity.__init__(self, created_by)
        self.nombres = nombres
        self.apellidos = apellidos
        self.tipo_doc = tipo_doc
        self.doc = doc
        self.correo = correo
        self.colegio = colegio
        self.celular = celular
        self.ano_estudio = ano_estudio
        self.id_distrito = id_distrito

    def to_json(self):
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "tipo_doc": self.tipo_doc,
            "doc": self.doc,
            "correo": self.correo,
            "colegio": self.colegio,
            "celular": self.celular,
            "ano_estudio": self.ano_estudio,
            "id_distrito": self.id_distrito,
            # "created_at": self.created_at.strftime('%Y-%m-%dT%H:%M:%S'),
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
