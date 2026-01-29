from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Detail(Base):
	__tablename__ = "t_dtlcode"

	id = Column(Integer,primary_key=True)
	codcde = Column(Integer,ForeignKey('t_entcde.codcde'), index=True)
	objet_id = Column(Integer, ForeignKey('t_objet.codobj'))
	qte = Column(Integer, default=1)
	commentaire = Column(String(100), default=None)