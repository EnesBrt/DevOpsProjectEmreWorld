# Utilise l'image Docker officielle pour Python 3.11.2
FROM python:3.11.2

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers du projet dans le répertoire de travail
COPY . /app

RUN mkdir -p /app/media

# Expose le port 8000
EXPOSE 8000

# Désinstalle et réinstalle django-filebrowser
RUN pip uninstall -y django-filebrowser
RUN pip install django-filebrowser

# Installe les autres dépendances de votre projet
RUN pip install -r requirements.txt

# Définit la commande à exécuter quand le conteneur démarre
CMD ["python", "/app/setup/manage.py", "runserver", "0.0.0.0:8000"]

