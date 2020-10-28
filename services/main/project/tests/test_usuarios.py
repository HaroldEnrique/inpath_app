# coding=utf-8
# services/main/project/tests/test_usuarios.py

import json
import unittest

from project.tests.base import BaseTestCase
from project import db
from project.api.model_usuarios import Persona

# just for testing
from datetime import datetime
#from sqlalchemy.sql import func

#def myconverter(o):
#    if isinstance(o, datetime):
#        return o.__str__()

def add_persona(nombres, ape_paterno, ape_materno, tipo_doc, doc, correo, colegio, celular, fecha_nac, created_by ):
    persona = Persona(
                    nombres=nombres,
                    ape_paterno=ape_paterno,
                    ape_materno=ape_materno,
                    tipo_doc=tipo_doc,
                    doc=doc,
                    correo=correo,
                    colegio=colegio,
                    celular=celular,
                    fecha_nac=fecha_nac,
                    created_by=created_by)

    db.session.add(persona)
    db.session.commit()
    return persona

class TestUsuarioService(BaseTestCase):
    """Pruebas para el servicio de usuarios."""

    def test_usuario(self):
        """Asegúrese de que la ruta /ping se comporte correctamente."""
        response = self.client.get('/usuarios/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success_usuarios', data['status'])
    
    def test_add_persona(self):
        """Ensure a new user can be added to the database."""
        with self.client:
            response = self.client.post(
                '/personas',
                data=json.dumps({
                    'nombres': 'nicole.garcia',
                    'ape_paterno': 'Da silva',
                    'ape_materno': 'Ramirez',
                    'tipo_doc':'dni',
                    'doc':123123,
                    'correo':'nicole.garcia@gmail.com',
                    'colegio':'IE 164',
                    'celular':127543578,
                    'fecha_nac':datetime.utcnow().__str__(),
                    'created_by':'test_script'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('nicole.garcia@gmail.com was added!', data['message'])
            self.assertIn('success', data['status'])
    
    def test_add_persona_invalid_json(self):
        """Asegúrese de que se produzca un error si el objeto JSON está vacío."""
        with self.client:
            response = self.client.post(
                '/personas',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_persona_invalid_json_keys(self):
        """
        Asegúrese de que se produzca un error si el objeto JSON no tiene una clave    
        de nombre de usuario.
        """
        with self.client:
            response = self.client.post(
                '/personas',
                data=json.dumps({'correo': 'nicole.garcia@gmail.com'}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_persona_duplicate_email(self):
        """ Asegúrese de que se arroje un error si el correo electrónico ya 
            existe."""
        with self.client:
            self.client.post(
                '/personas',
                data=json.dumps({
                    'nombres': 'nicole.garcia',
                    'ape_paterno': 'Da silva',
                    'ape_materno': 'Ramirez',
                    'tipo_doc':'dni',
                    'doc':123123,
                    'correo':'nicole.garcia@gmail.com',
                    'colegio':'IE 164',
                    'celular':127543578,
                    'fecha_nac':datetime.utcnow().__str__(),
                    'created_by':'test_script'
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/personas',
                data=json.dumps({
                    'nombres': 'nicole.garcia',
                    'ape_paterno': 'Da silva',
                    'ape_materno': 'Ramirez',
                    'tipo_doc':'dni',
                    'doc':123123,
                    'correo':'nicole.garcia@gmail.com',
                    'colegio':'IE 164',
                    'celular':127543578,
                    'fecha_nac':datetime.utcnow().__str__(),
                    'created_by':'test_script'
                }),
                content_type='application/json',
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Sorry. That email already exists.', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_persona(self):
        """Ensure get single user behaves correctly."""
        persona = add_persona('nombres', 'ape_paterno', 'ape_materno', 'tipo_doc', 654654654,
                              'correo@gmail.com', 'colegio', 765765765, datetime.utcnow(),'test_script')
        with self.client:
            response = self.client.get(f'/personas/{persona.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('nombres', data['data']['nombres'])
            self.assertIn('correo@gmail.com', data['data']['correo'])
            self.assertIn('success', data['status'])
    
    def test_single_persona_no_id(self):
        """Asegúrese de que se produzca un error si no se proporciona un id."""
        with self.client:
            response = self.client.get('/personas/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Persona does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_persona_incorrect_id(self):
        """Asegúrese de que se produzca un error si el id no existe."""
        with self.client:
            response = self.client.get('/personas/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Persona does not exist', data['message'])
            self.assertIn('fail', data['status'])


    def test_all_personas(self):
        """Asegúrese de que todos los usuarios se comporten correctamente."""

        add_persona('luccia', 'gamarra', 'perez', 'passport', 654654654,
                    'luccia@gmail.com', 'colegio1', 765765765, datetime.utcnow(),'test_script')
        add_persona('nicole', 'gamarra', 'perez', 'dni', 654654654,
                    'nicole@gmail.com', 'colegio2', 765765765, datetime.utcnow(),'test_script')
        add_persona('julian', 'gamarra', 'perez', 'dni', 654654654,
                    'julian@gmail.com', 'colegio3', 765765765, datetime.utcnow(),'test_script')
        
        with self.client:
            response = self.client.get('/personas')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['personas']), 3)
            self.assertIn('luccia', data['data']['personas'][0]['nombres'])
            self.assertIn(
                'luccia@gmail.com', data['data']['personas'][0]['correo'])
            self.assertIn('nicole', data['data']['personas'][1]['nombres'])
            self.assertIn(
                'nicole@gmail.com', data['data']['personas'][1]['correo'])
            self.assertIn('julian', data['data']['personas'][2]['nombres'])
            self.assertIn(
                'julian@gmail.com', data['data']['personas'][2]['correo'])
            self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()