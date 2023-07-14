from typing import List, Dict
from fastapi import FastAPI
from pydantic import BaseModel, Field, RootModel

app = FastAPI(title='Insurance calc')
rates = {'2020-06-01': [
    {'cargo_type': 'Glass', 'rate': '0.04'},
    {'cargo_type': 'Other', 'rate': '0.01'}
]}

class CargoRate(BaseModel):
    cargo_type: str
    rate: float


class DailyRate(RootModel):
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

