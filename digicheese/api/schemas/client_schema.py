from pydantic import BaseModel
from typing import Optional


class ClientBase(BaseModel):
    """Base schema for client data."""
    nom: str
    prenom: str
    genre: Optional[str] = None
    adresse: str
    complement_adresse: Optional[str] = None
    tel: Optional[str] = None
    email: Optional[str] = None
    newsletter: Optional[int] = 0


class ClientPost(ClientBase):
    """Schema for creating a new client."""
    pass


class ClientPatch(ClientBase):
    """Schema for updating an existing client."""
    nom: Optional[str] = None
    prenom: Optional[str] = None
    adresse: Optional[str] = None


class ClientInDB(ClientBase):
    """Schema for client data stored in the database."""
    codcli: int
    
    class Config:
        from_attributes = True