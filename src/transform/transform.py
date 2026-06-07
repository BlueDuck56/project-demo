import pandas as pd
import json


class DataTransformer:
    def __init__(self, raw_data: dict):
        self.raw_data = raw_data

    def transform(self) -> pd.DataFrame:
        items = self.raw_data.get("itemSummaries", [])
        transformed_data = []
        for item in items:
            transformed_item = {
                "title": item.get("title"),
                "price": item.get("price", {}).get("value"),
                "currency": item.get("price", {}).get("currency"),
                "condition": item.get("condition"),
                "item_id": item.get("itemId"),
                "image_url": item.get("image", {}).get("imageUrl"),
                "item_web_url": item.get("itemWebUrl"),
            }
            transformed_data.append(transformed_item)
        return pd.DataFrame(transformed_data)
