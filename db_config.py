"""Config for T-ORM."""

from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from main import app


async def init_db():
    await Tortoise.init(
        db_url="postgres://myuser:mypassword@db:5432/mydatabase",
        modules={"models": ["models"]},
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.on_event("shutdown")
async def on_shutdown():
    await close_db()


TORTOISE_ORM = {
    "debug": True,
    "connections": {
        "default": "postgres://myuser:mypassword@db:5432/mydatabase",
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=True,
)
