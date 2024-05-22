import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    nombre = Column(String)
    apellido = Column(String)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    posts = relationship('Post', back_populates='usuario')
    comentarios = relationship('Comentario', back_populates='usuario')
    likes = relationship('Like', back_populates='usuario')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    contenido = Column(Text)
    imagen = Column(String)
    usuario = relationship('Usuario', back_populates='posts')
    comentarios = relationship('Comentario', back_populates='post')
    likes = relationship('Like', back_populates='post')

class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    contenido = Column(Text, nullable=False)
    post = relationship('Post', back_populates='comentarios')
    usuario = relationship('Usuario', back_populates='comentarios')

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    post = relationship('Post', back_populates='likes')
    usuario = relationship('Usuario', back_populates='likes')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
