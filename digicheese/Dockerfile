# 1. Utiliser Python 3.11 comme base
FROM python:3.11
# 2. Définir le répertoire de travail dans le conteneur
WORKDIR /code
# 3. Copier le fichier requirements.txt
COPY requirements.txt .
# 4. Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt
# 5. Exposer le port 80
EXPOSE 80
# 6. Lancer l'application FastAPI avec Uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "api"]