from typing import Dict, List
from fastapi import FastAPI
from pydantic import BaseModel, Field, RootModel
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


app = FastAPI(title='Insurance calc')


class CargoRate(BaseModel):
    """Submodel for DailyRate model."""

    cargo_type: str
    rate: str = '0.1'


class DailyRate(RootModel):
    """Model represents daily rates for cargo types."""

    root: Dict[str, List[CargoRate]] = Field(examples=[{
        '2020-06-01': [
            {'cargo_type': 'Glass', 'rate': '0.01'},
            {'cargo_type': 'Other', 'rate': '0.02'}
        ]
    }])


@app.post('/add_tariff')
async def add_tariff(root: DailyRate):
    for date in root.model_dump():
        print(date)
        print()
    print(type(root.model_dump()))
    return {'status': 200, 'result': root}


@app.post('/get_price')
async def get_rate(cargo_type: str, date: str, cost: float):
    print(cargo_type, date, cost)
    return {'status': 200, 'result': [cargo_type, date, cost]}


# register_tortoise(
#     app,
#     db_url="postgres://myuser:mypassword@localhost:5432/mydatabase",
#     modules={"models": ['models']},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
