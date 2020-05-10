import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


env_path = Path(__file__).parent.absolute() / '.env'

load_dotenv(dotenv_path=env_path)

#variables de conexion
dbnamemaster= os.getenv('DB_NAME_MASTER')
dbusermaster = os.getenv('DB_USER_MASTER')
dbpassword = os.getenv('DB_PASSWORD_MASTER')

#variables de nombre de la base
dbname= os.getenv('DB_NAME')
dbuser=os.getenv('DB_USER')

print('(+) Database connection started')
psqlCon = psycopg2.connect(
	"dbname=%s user=%s password=%s" %(dbnamemaster,dbusermaster,dbpassword)
);

print('(+) Database connection ended')

print('(+) Query to database started')
psqlCon.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
psqlCursor= psqlCon.cursor();

print('(+) Desconected to database started')
desconected ="select pg_terminate_backend(pg_stat_activity.pid) from pg_stat_activity where pg_stat_activity.datname =  '%s' AND pid <> pg_backend_pid();"%(dbname)
psqlCursor.execute(desconected);
print('(+) Desconected to database ended')

print('(+) Query deleted dabatase started')
deleteDatabase = "DROP DATABASE IF EXISTS %s ;" %(dbname)
psqlCursor.execute(deleteDatabase);
print('(+) Query deleted dabatase ended')

print('(+) Query created dabatase started %s' %dbname)
createDatabase = "CREATE DATABASE %s OWNER %s;" %(dbname,dbuser)
psqlCursor.execute(createDatabase);
print('(+) Query created dabatase ended')

print('(+) Query to database ended %s' %dbname)

psqlCursor.close();

psqlCon.close();
print('(+) Database connection ended')