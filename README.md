# About
This is my test exercise for Python middle developer's vacancy for SMIT.Studio company.

## Main packeges:
- FastAPI
- SqlAlchemy
- Postgresql
- Docker / Compose
- pytest
- pydantic / pydantic-settings
- poetry


## Map
There is first looking need to docs. Here will write structure of app, UML schemas etc.

## Quick start
First, you need update your .env, rename .env-example, from root dir do it:
```shell
mv src/.env-example src/.env
```
 and look, that it is parsed, from root dir do:
```shell
python settings.py
``` 
You will get some:
```shell
{'db': {'host': 'localhost', 'port': 5432, 'user': 'postgres', 'passwd': 'postgres', 'name': 'smit'}}
```
if you don't see that, you need to correct your .env or see settings.py and DatabaseSetting class.


For quick start of app you need to start a docker-compose from root of project, the command for this:
```shell
docker-compose -f ./docker/docker-compose.yml --build -d
```
or if you want to see the all, than you need to remove "-d" key.