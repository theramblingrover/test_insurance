# Insurance calc (test task)

## Test project for interview.

Simple REST API provides calculation of insuranse rates for differen types of cargos depends on the date.
## Stack: 
- Python
- FastAPI
- Pydantic
- Tortoise ORM
- Aerich
- Docker compose
- PostgreSQL


To run locally perform 
```
docker compose up 
```
in the root folder of the project

First it will bring up DB service, next step applies midrations to database and finally API will start.

Access it on 

```
http://localhost:8000

```

Try 
```
http://localhost:8000/docs
```

to learn about endpoints and schemas
