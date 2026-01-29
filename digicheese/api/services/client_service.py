from sqlalchemy.orm import Session
from ..repositories import ClientRepository
from ..schemas import ClientPost, ClientPatch

class ClientService:
    """Service class for managing client operations.
    
    Receive a schema from router and return a dictionary to repository."""

    def __init__(self):
        self.repository = ClientRepository()
    
    def __traitement(self, client: dict):
        return client
    
    
    def get_all_clients(self, db: Session):
        return self.repository.get_all_clients(db)
    
    
    def get_client_by_id(self, db: Session, client_id: int):
        return self.repository.get_client_by_id(db, client_id)
    
    
    def create_client(self, db: Session, new_client: ClientPost):
        new_client = new_client.model_dump()
        new_client = self.__traitement(new_client)
        return self.repository.create_client(db, new_client)
    
    
    def patch_client(self, db: Session, client_id: int, client: ClientPatch):
        client = client.model_dump(exclude_unset=True)
        client = self.__traitement(client)
        return self.repository.patch_client(db, client_id, client)
    
    
    def delete_client(self, db: Session, client_id: int):
        return self.repository.delete_client(db, client_id)