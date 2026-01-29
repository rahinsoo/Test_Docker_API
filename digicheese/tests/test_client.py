from fastapi import Response
from fastapi.testclient import TestClient
import pytest


# Constantes pour l'endpoint
CLIENT_ENDPOINT = "/api/v1/client"


@pytest.fixture
def client_data():
    """Données de test pour créer un client."""
    return {
        "nom": "Doe",
        "prenom": "John",
        "genre": "M",
        "adresse": "123 rue de la Paix",
        "complement_adresse": "Batiment b",
        "tel": "01.23.45.67.89",
        "email": "John.Doe@gmail.com",
        "newsletter": 1,
    }


def test_get_all_clients(client: TestClient):
    """Tester l'obtention de tous les clients (doit renvoyer une liste vide au début)."""
    response: Response = client.get(CLIENT_ENDPOINT)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_create_client(client: TestClient, client_data):
    """Tester la création d'un client."""
    response: Response = client.post(CLIENT_ENDPOINT, json=client_data)
    assert response.status_code == 201
    
    data = response.json()
    del data["codcli"]
    assert data == client_data  


def test_get_client_by_id(client: TestClient, client_data):
    """Tester la récupération d'un client par son ID."""
    
    # Créer un client
    client.post(CLIENT_ENDPOINT, json=client_data)
    
    # Récupérer le client par ID
    response: Response = client.get(f"{CLIENT_ENDPOINT}/1")
    assert response.status_code == 200
    
    data = response.json()
    del data["codcli"]
    assert data == client_data  


def test_patch_client_by_id(client: TestClient, client_data):
    """Tester la mise à jour partielle des informations d'un client."""
    
    # Créer un client
    client.post(CLIENT_ENDPOINT, json=client_data)
    
    new_data = {
        "complement_adresse": "Batiment C"
    }
    
    response: Response = client.patch(f"{CLIENT_ENDPOINT}/1", json=new_data)
    assert response.status_code == 200
    assert response.json()["complement_adresse"] == "Batiment C"



def test_delete_client_by_id(client: TestClient, client_data):
    """Tester la suppression d'un client par son ID."""

    # Créer un client
    client.post(CLIENT_ENDPOINT, json=client_data)

    # Supprimer le client
    response: Response = client.delete(f"{CLIENT_ENDPOINT}/1")
    assert response.status_code == 200  # OK

    # Vérifier que le client n'existe plus
    response: Response = client.get(f"{CLIENT_ENDPOINT}/1")
    assert response.status_code == 404 # Not Found