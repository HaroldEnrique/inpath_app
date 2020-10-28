# coding=utf-8
# services/main/project/api/entity.py

from datetime import datetime
#from sqlalchemy import create_engine, Column, String, Integer, DateTime
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker

from project import db

# db_url = 'localhost:5432'
# db_name = 'online-exam'
# db_user = 'postgres'
# db_password = '0NLIN3-ex4m'
# engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
# Session = sessionmaker(bind=engine)
# 
# Base = declarative_base()


class Entity():
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    last_updated_by = db.Column(db.String(128))

    def __init__(self, created_by):
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.last_updated_by = created_by