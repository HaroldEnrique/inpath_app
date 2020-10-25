
from sqlalchemy.sql import func
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
    activo = db.Column(db.Integer, nullable=False)
    # created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, nombres, ape_paterno, ape_materno, tipo_doc, doc, correo, colegio, celular, fecha_nac, activo, created_by):
        Entity.__init__(self, created_by)
        self.nombres = nombres
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.tipo_doc = tipo_doc
        self.correo = correo
        self.colegio = colegio
        self.celular = celular
        self.fecha_nac = fecha_nac
        self.activo = activo
    
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
            "fecha_nac": self.fecha_nac,
            "activo": self.activo
        }


class Usuario(db.Model):

    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    activo = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    persona_id = db.Column(db.Integer, db.ForeignKey(Persona.__table__.c['id']))

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "active": self.active,
        }

    def __init__(self, username, email):
        self.username = username
        self.email = email
