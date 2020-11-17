# coding=utf-8
# services/main/manage.py

import sys
import unittest
import coverage

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.model_usuarios import Persona
from project.api.model_encuesta import TipoEncuesta, Encuesta,TipoPregunta,Pregunta,Opcion

# just for testing
from datetime import datetime

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Ejecuta las pruebas sin cobertura de código"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)

@cli.command('seed_db')
def seed_db():
    """Siembra la base de datos."""

    db.session.add(TipoEncuesta(
        nombre="tipo_academico",
        created_by="seed script"))

    db.session.add(TipoEncuesta(
        nombre="tipo_vocacional",
        created_by="seed script"))
    
    db.session.commit()

    db.session.add(Encuesta(
        nombre="Academico 3 anho",
        descripcion="aplicado para Buen Pastor",
        estado=1,
        id_tipo_encuesta=1,
        created_by="seed script"
    ))

    db.session.add(Encuesta(
        nombre="Academico 2 anho",
        descripcion="aplicado para Canto Rey",
        estado=0,
        id_tipo_encuesta=1,
        created_by="seed script"
    ))

    db.session.commit()

    db.session.add(TipoPregunta(
        tipo="respuesta corta",

        created_by="seed script"))

    db.session.add(TipoPregunta(
        tipo="varias opciones",
        created_by="seed script"))

    db.session.commit()

    db.session.add(Pregunta(
        pregunta="¿Cual es tu apellido?",
        tamanho = 50,
        id_tipo_pregunta = 1,
        id_test = 1,
        created_by="seed script"))

    db.session.add(Pregunta(
        pregunta="¿Cual es tu nombre?",
        tamanho = 50,
        id_tipo_pregunta = 1,
        id_test = 1,
        created_by="seed script"))

    db.session.add(Pregunta(
        pregunta="¿Tuviste algún problema de salud?",
        tamanho = 50,
        id_tipo_pregunta = 1,
        id_test = 1,
        created_by="seed script"))
    
    db.session.commit()

    db.session.add(Opcion(
        texto="Nunca",
        id_pregunta = 3,
        created_by="seed script"))

    db.session.add(Opcion(
        texto="Tal vez",
        id_pregunta = 3,
        created_by="seed script"))

    db.session.add(Opcion(
        texto="Siempre",
        id_pregunta = 3,
        created_by="seed script"))

    db.session.commit()

    db.session.add(Persona(
        nombres="Carlos Tito",
        ape_paterno="Covid",
        ape_materno="2020",
        tipo_doc="dni",
        doc=543543,
        correo="covid@gmail.com",
        colegio="colegio",
        celular=123123123,
        fecha_nac=datetime.utcnow(),
        created_by="seed script"))
    db.session.add(Persona(
        nombres="Norma Luccia",
        ape_paterno="Covid",
        ape_materno="2020",
        tipo_doc="dni",
        doc=543543,
        correo="norma@gmail.com",
        colegio="colegio2",
        celular=654654654,
        fecha_nac=datetime.utcnow(),
        created_by="seed script"))

    db.session.commit()


@cli.command()
def cov():
    """Ejecuta las pruebas unitarias con cobertura."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)



if __name__ == '__main__':
    cli()