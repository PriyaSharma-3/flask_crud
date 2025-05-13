# flask_crud_using_postgresql
###### This web application is built using the Python Flask framework, HTML+CSS, JQuery and postgresql database.

###### To run this code, you must have the following installed on your computer:
###### * python installed
###### * postgresql database
###### * postgresql server
###### * Flask
###### * flask_postgresqldb

###### * Getting Started
###### * Download links:

SSH clone URL: git@github.com:PriyaSharma-3/flask_crud.git

HTTPS clone URL: https://github.com/PriyaSharma-3/flask_crud.git

###### * Install postgressql
Download and install PostgreSQL from PostgresApp.
Download and install the PostgreSQL admin tool pgAdmin.

###### * You can also download from https://postgresapp.com/downloads.html

Download and install postgressql admin tool
https://www.postgresql.org/ftp/pgadmin/pgadmin4/v6.18/macos/ 

###### * Add new server in pgadmin

Open pgAdmin and add a new server.
Create a database

psql postgres
CREATE DATABASE flask_crud; # Create dataabase


###### * Create virtual environment 
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

###### * export python libraries if installed any
pip freeze > requirements.txt


###### * Create .env file

DB_HOST=localhost
DB_PORT=5432
DB_NAME=flask_crud
DB_USER=postgres
DB_PASSWORD=new_secure_password


###### * run this project by this command
###### flask --app app.py run