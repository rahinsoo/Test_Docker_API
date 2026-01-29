import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from api.main import app
from api.database import get_db
from api.models import Base

# Configuration de la base de données de test
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function", autouse=True)
def setup_database():
    """Fixture pour configurer la base de données avant chaque test."""
    Base.metadata.drop_all(bind=engine)  # Supprimer les tables avant chaque test
    Base.metadata.create_all(bind=engine)  # Recréer les tables
    yield
    Base.metadata.drop_all(bind=engine)  # Nettoyage après le test


def override_get_db():
    """Override pour injecter une session de test dans les dépendances."""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# Client de test
@pytest.fixture(scope="module")
def client():
    """Fixture qui fournit un client TestClient pour chaque test."""
    return TestClient(app)