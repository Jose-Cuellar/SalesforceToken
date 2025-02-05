Salesforce Token Generator

Este proyecto permite obtener un Access Token de Salesforce utilizando la autenticación basada en OAuth 2.0.

Requisitos:
1. Antes de ejecutar el proyecto, asegúrate de tener lo siguiente:
    - Python 3.8.10 instalado
    - Dependencias necesarias (listadas abajo)
    - Una cuenta de Salesforce y acceso a una aplicación conectada con OAuth habilitado


Instalación:

1. Clonar el repositorio:
    - git clone https://github.com/Jose-Cuellar/SalesforceToken.git
    - cd SalesforceToken

2. Instalar las dependencias:
    Nota: Asegúrate de tener instalado pip3, y luego instala las librerías necesarias para el proyecto. Si no tienes un entorno virtual, puedes instalar las dependencias globalmente:
    - pip3 install -r requirements.txt

    Si prefieres usar un entorno virtual, puedes hacerlo de la siguiente manera:
    - python -m venv venv
    - source venv/bin/activate  # En Windows usa 'venv\Scripts\activate'
    - pip install -r requirements.txt


Uso

1. Obtener los datos necesarios de Salesforce:

    Asegúrate de tener los siguientes datos de tu aplicación conectada en Salesforce:
    - Client ID: El ID de cliente de tu aplicación conectada en Salesforce.
    - Client Secret: El secreto del cliente de tu aplicación conectada en Salesforce.
    - Refresk Token: Token de actualización para solicitar un nuevo access token.
    - Tú instancia de Salesforce.


2. Obtener el Access Token:

    Ejecuta el script para obtener el access token:
    - flask --app app run
    - Ir a la ruta http://127.0.0.1:5000 en el navegador.
    - Dar click sobre "Obtener token" para solicitar un access token a tú instancia de Salesforce.
