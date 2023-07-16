from typing import Dict, List
from fastapi import FastAPI
from pydantic import BaseModel, Field, RootModel
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

from models import DateRate, CargoType


app = FastAPI(title="Insurance calc")



class CargoRate(BaseModel):
    """Submodel for DailyRate model."""

    cargo_type: str
    rate: str


class DailyRate(RootModel):
    """Model represents daily rates for cargo types."""

    root: Dict[str, List[CargoRate]] = Field(
        examples=[
            {
                "2020-06-01": [
                    {"cargo_type": "Glass", "rate": "0.01"},
                    {"cargo_type": "Other", "rate": "0.02"},
                ]
            }
        ]
    )


class InsurPrice(BaseModel):
    price: float
    cost: float
    rate: float
    date: str
    cargo_type: str


async def create_tariff(data: Dict[List, DailyRate]):
    for date in data.keys():
        for item in data[date]:
            cargo, created = await CargoType.get_or_create(
                name=item['cargo_type'].lower()
                )
            if created:
                await cargo.save()
            date_rate, created = await DateRate.get_or_create(
                date=date,
                cargo=cargo,
                rate=item['rate']
                )
            if created:
                await date_rate.save()
    


@app.post("/add_tariff")
async def add_tariff(root: DailyRate):
    print(root)
    await create_tariff(root.model_dump())
    return {"status": 200, "result": root}


@app.get("/get_price")
async def get_rate(cargo_type: str, date: str, cost: float):
    print(cargo_type, date, cost)
    cargo = (await CargoType.filter(
        name=cargo_type
        ).select_related('rates').filter(rates__date=date) or
    await CargoType.filter(
        name="Other"
        ).select_related('rates').filter(rates__date=date))
    return InsurPrice(
        price=float(cargo[0].rates.rate)*cost,
        cost=cost,
        rate=cargo[0].rates.rate,
        date=date,
        cargo_type=cargo[0].name
    )


register_tortoise(
    app,
    db_url="postgres://myuser:mypassword@localhost:5432/mydatabase",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
