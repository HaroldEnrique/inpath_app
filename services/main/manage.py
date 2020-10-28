# coding=utf-8
# services/main/manage.py

import sys
import unittest
import coverage

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.model_usuarios import Persona

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

