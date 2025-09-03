# tui-proyectoFinal

Este es el proyecto final del grupo 1 para la materia TUI.

## Instalación y puesta en marcha

1. Clona el repositorio:
   ```
   git clone https://github.com/josemanuelborras/tui-proyectoFinal.git
   ```
2. Ingresa a la carpeta del proyecto:
   ```
   cd tui-proyectoFinal
   ```
3. Instala las dependencias necesarias:
   ```
   pip install django mysqlclient
   ```
   - **django**: Framework principal (si no lo tienes)
   - **mysqlclient**: Conector para usar MySQL con Django

4. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```
5. Abre tu navegador y accede a [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Estructura recomendada de templates

- **components/** → Elementos básicos (button, input, etc.)
- **sections/** → Agrupaciones de componentes (header, footer, card, etc.)
- **layouts/** → Estructuras generales de página

Esta organización permite reutilizar y mantener ordenados los elementos de UI/UX en todo el proyecto.

## Librerías necesarias

- django
- mysqlclient

Para instalar todas las dependencias necesarias, ejecuta el siguiente comando en la terminal:
```
pip install django mysqlclient
```

## Versiones utilizadas

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

## Uso

Para correr la aplicación, ejecuta el siguiente comando en la terminal:
```
python manage.py runserver
```

Una vez iniciado el servidor, podrás ver la página de bienvenida de Django. Desde aquí puedes comenzar a desarrollar tu aplicación.

## Contribución

Si deseas contribuir, por favor haz un fork del repositorio y envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.
