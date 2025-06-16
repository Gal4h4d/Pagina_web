# Proyecto Página Web - Django

Este es un proyecto de ejemplo desarrollado con Django. Su objetivo es ser una base para una página web donde se pueden gestionar noticias u otros contenidos estáticos y dinámicos.

## Características

- Backend en Django
- Base de datos SQLite3 por defecto (`se puede usar PostgreSQL`)
- Gestión de archivos estáticos y media
- Uso de plantillas HTML (`templates/base.html`)
- Separación de configuraciones sensibles usando `.env` y `secret.json`

## Requisitos

- Python 3.8 o superior
- pip
- virtualenv (opcional pero recomendado)

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/proyecto_django.git
cd proyecto_django
```
Crea un entorno virtual (opcional pero recomendado):

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

instala las dependencias:

pip install -r requirements.txt

Aplica las migraciones y ejecuta el servidor:

python manage.py migrate
python manage.py runserver
