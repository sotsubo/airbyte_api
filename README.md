# airbyte

cd airbyte_api
docker-compose up

# source-book
cd airbyte_api/airbyte-integrations/connectors/source-book

docker build . -t airbyte/source-book:dev
docker run --rm -i airbyte/source-book:dev spec

# mysqlserver 

docker pull mysql:8
docker run --name=mysql1 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123  -d mysql:8 
# Connect to mysql and create a database and user with privileges
create database hodinkee;
CREATE USER 'hodinkee' IDENTIFIED BY 'hodinkee';
GRANT ALL PRIVILEGES ON *.* TO 'hodinkee';

