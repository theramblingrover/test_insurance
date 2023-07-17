import random
import json

data = {
    "2022-10-07": [
        {"cargo_type": "Glass", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Plastic", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Metal", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Textiles", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Electronics", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Chemicals", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Other", "rate": str(round(random.uniform(0.01, 0.1), 2))},
    ],
    "2022-11-07": [
        {"cargo_type": "Glass", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Plastic", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Metal", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Textiles", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Electronics", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Chemicals", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Other", "rate": str(round(random.uniform(0.01, 0.1), 2))},
    ],
    "2022-12-07": [
        {"cargo_type": "Glass", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Plastic", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Metal", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Textiles", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Electronics", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Chemicals", "rate": str(round(random.uniform(0.01, 0.1), 2))},
        {"cargo_type": "Other", "rate": str(round(random.uniform(0.01, 0.1), 2))},
    ]
}

print(json.dumps(data))