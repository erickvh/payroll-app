# PayrollApp

Aplicación asignada en materia base de datos con tecnologias Python y PostgreSQL en el Backend

## Comenzando
Los siguientes requerimientos se deben seguir para instalar la aplicación para desarrollo.


### Prerequisitos
Lo que debes tener instalador para poder correr el proyecto.

* python >= 3.6
* pip >= 19.0
* PostgreSQL >= 9.0
* Git >= 2.0
* Cmder 


### instalación

Después de cumplir todos los requisitos se debe instalar.

1. Primero se debe clonar el proyecto actual.
    ```

    git clone https://github.com/erickv94/payrollApp.git

    ```
2. Luego se debe acceder a la carpeta raiz del directorio clonado e instalar las dependencias.
    ```
        pip install -r requirements.txt
    ```
3. Luego se debe realizar una copia del archivo **.env.example**  con el nombre **.env**
    ```
        cp .env.example
    ```



4. Luego de esto sin tener ningun problema, se debe modificar el archivo .env recientemente copiado 
con las variables de entorno de su preferencia de acuerdo a su base de datos.

```
    DB_NAME=payroll
    DB_USER=payroll
    DB_HOST=127.0.0.1
    DB_PORT=5432
    DB_PASSWORD=secret

```
5. luego de modificar el archivo **.env** se debe correr las migraciones junto a los datos semillas

```
    python manage.py migrate
    python load_fixtures.py
```
