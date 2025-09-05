# tui-proyectoFinal

Este es el proyecto final del grupo 1 para la carrera Tecnicatura Universitaria en Informatica.
Universidad Nacional del Nordeste.

## Instalación y puesta en marcha
1. Clona el repositorio:
   ```
   git clone https://github.com/josemanuelborras/tui-proyectoFinal.git
   ```
   ### Versiones utilizadas
   - Python: 3.13.7
   - Django: 5.2.5

   ### Cómo verificar las versiones
   Para ver la versión de Python:
   ```
   python --version
   ```
   Para ver la versión de Django:
   ```
   python -m django --version
   ```

2. Ingresa a la carpeta del proyecto:
   ```
   cd tui-proyectoFinal
   ```

3. Instala las dependencias necesarias:
   ### Librerías necesarias
  - **django**: Framework principal (si no lo tienes)
  - **mysqlclient**: Conector para usar MySQL con Django
  - **python-dotenv**: Permite cargar variables de entorno desde un archivo `.env`
   ```
   pip install django mysqlclient python-dotenv
   ```
   
4. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

5. Abre tu navegador y accede a [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Uso
Para correr la aplicación, ejecuta el siguiente comando en la terminal:
```
python manage.py runserver
```
Una vez iniciado el servidor, podrás ver la página de bienvenida de Django. Desde aquí puedes comenzar a desarrollar tu aplicación.

## Estructura recomendada de templates
- **components/** → Elementos básicos (button, input, etc.)
- **sections/** → Agrupaciones de componentes (header, footer, card, etc.)
- **layouts/** → Estructuras generales de página

Esta organización permite reutilizar y mantener ordenados los elementos de UI/UX en todo el proyecto.

## Antes de cada actualizacion
Correr los comandos:
```
python manage.py makemigrations
```
- Detecta los cambios en tus modelos y crea archivos de migración.
```
python manage.py migrate
```
- Aplica esos cambios a la base de datos, creando o actualizando las tablas según corresponda.

## Integración con la base de datos
### Instalar MySQL Server
   - [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
   - Recordar contraseña
   - Correr el comando
   ```
   mysql -u root -p
   ```
   - Ingresar contraseña
   - Correr el comando
   ```
   CREATE DATABASE gestionAcademica;
   ```
   - Verificar la creación de la base de datos
   ```
   SHOW DATABASES;
   ```
   - Correr el comando
   ```
   python manage.py migrate para crear y actualizar las tablas
   ```

### Crear tabla Admin
1. Correr el comando e ingresar la constraseña:
   ```
   mysql -u root -p
   ```
2. Acceder a la base de datos gestionAcademica:
   ```
   USE gestionAcademica
   ```
3. Insertar datos de usuario y constraseña:
   ```
   INSERT INTO adminPanel_admin (usuario, password) VALUES ('usuario', 'constraseña');
   ```
4. Controlar que los datos existan:
   ```
   select * from adminpanel_admin;
   ```

## Variables de entorno
  - Crear un nuevo archivo .env en la carpeta raíz

### En desarrollo
- SECRET_KEY=clavesecreta
- DEBUG=True
- DB_NAME=gestionAcademica
- DB_USER=root
- DB_PASSWORD=1234
- DB_HOST=localhost
- DB_PORT=3306

## Rutas
### Admin
- /adminPanel

## Contribución

Si deseas contribuir, por favor haz un fork del repositorio y envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT y de la UNNE.
