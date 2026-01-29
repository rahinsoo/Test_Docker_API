from sqlalchemy import Column, Integer, String
from .base import Base

class Client(Base):
	__tablename__ = "t_client"

	codcli = Column(Integer, primary_key=True)
	nom = Column(String(40), index=True)
	prenom = Column(String(30))
	genre = Column(String(8), default=None)
	adresse = Column(String(50))
	complement_adresse = Column(String(50), default=None)
	tel = Column(String(10), default=None)
	email = Column(String(255), default=None)
	newsletter = Column(Integer, default=0)