# Utilise l'image Docker officielle pour Python 3.11.2
FROM python:3.11.2

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers du projet dans le répertoire de travail
COPY . /app

# Installe les dépendances
RUN pip install -r /app/requirements.txt

# Expose le port 8000
EXPOSE 8000

# Définit la variable d'environnement DJANGO_SETTINGS_MODULE
ENV DJANGO_SETTINGS_MODULE=setup.settings

# Lance le serveur web
CMD ["python", "/app/setup/manage.py", "runserver", "0.0.0.0:8000"]

