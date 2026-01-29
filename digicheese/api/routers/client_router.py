"""
References all client-related endpoints in the FastAPI application.

Receives requests from the client router, transform in client schema and processes them using the ClientService.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import ClientPost, ClientPatch, ClientInDB
from ..database import get_db
from ..services import ClientService

# Create a router for client-related endpoints
router = APIRouter(prefix="/client", tags=["client"])

# Initialize the client service to have access to client operations
service = ClientService()

@router.get("/", status_code=200, response_model=list[ClientInDB])
def get_clients(db: Session=Depends(get_db)):
    return service.get_all_clients(db)
    

@router.get("/{client_id}", status_code=200, response_model=ClientInDB)
def get_client(client_id: int, db: Session=Depends(get_db)):
    client = service.get_client_by_id(db, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return client


@router.post("/", status_code=201, response_model=ClientInDB)
def create_client(donnees_client: ClientPost, db: Session=Depends(get_db)):
    return service.create_client(db, donnees_client)


@router.patch("/{client_id}", status_code=200, response_model=ClientInDB)
def patch_client(client_id: int, donnees_client: ClientPatch, db: Session=Depends(get_db)):
    client = service.get_client_by_id(db, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return service.patch_client(db, client_id, donnees_client)


@router.delete("/{client_id}", status_code=200, response_model=ClientInDB)
def delete_client(client_id: int, db: Session=Depends(get_db)):
    client = service.get_client_by_id(db, client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return service.delete_client(db, client_id)