
from sqlalchemy.sql import func

from project import db

class Persona(db.Model):
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
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

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
