# Insurance calc (test task)

## Test project for job interview.

Simple REST API provides calculation of insuranse rates for differen types of cargos depends on the date.
## Tech stack: 
- Python
- FastAPI
- Pydantic
- Tortoise ORM
- Aerich
- Docker compose
- PostgreSQL


To run locally perform 
```
docker compose up db
```
in the root folder of the project.

Make sure if database accepts connections and run migrations if nessesary:

```
docker compose up automigrate
```

and now we can start API service:

```
docker compose up backend
```

First we bring up DB service, next step applies migrations to database and finally API will start.

Access API on <http://localhost:8000>.


Try <http://localhost:8000/docs> to learn about endpoints and schemas.

```gendata.py``` generates dates, cargo types and rates. Run it and copy output to Postman/Swagger to fill database.
