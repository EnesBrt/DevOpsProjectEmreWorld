# Utilise l'image Docker officielle pour Python 3.11.2
FROM python:3.11.2

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers du projet dans le répertoire de travail
COPY . /app

# Crée le répertoire media dans le conteneur
RUN mkdir -p /app/media/uploads

# Change les permissions du répertoire media
RUN chmod -R 777 /app/media/uploads

# Expose le port 8000
EXPOSE 8000

# Installe les dépendances
RUN pip install -r /app/requirements.txt

# Définit un volume pour le répertoire media
VOLUME /app/media/uploads

# Lance le serveur web
CMD ["python", "/app/setup/manage.py", "runserver", "0.0.0.0:8000"]

