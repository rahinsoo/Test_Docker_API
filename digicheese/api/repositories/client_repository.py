from ..models import Client
from sqlalchemy.orm import Session


class ClientRepository:
    """Repository class for managing client operations in the database.

    Receive a dictionary from service, save it to the database and return the client model to service."""
    
    def get_all_clients(self, db: Session):
        return list(db.query(Client).all())
    
    def get_client_by_id(self, db: Session, id: int):
        return db.query(Client).get(id)
    
    def create_client(self, db: Session, donnees_client: dict):
        client = Client(**donnees_client)
        db.add(client)
        db.commit()
        db.refresh(client)
        return client
    
    def patch_client(self, db: Session, id: int, donnees_client: dict):
        client = db.query(Client).get(id)
        for key, value in donnees_client.items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
        return client
    
    def delete_client(self, db: Session, id: int):
        client = db.query(Client).get(id)
        db.delete(client)
        db.commit()
        return client