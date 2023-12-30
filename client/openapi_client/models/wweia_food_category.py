# coding: utf-8

"""
    Food Data Central API

    The FoodData Central API provides REST access to FoodData Central (FDC). It is intended primarily to assist application developers wishing to incorporate nutrient data into their applications or websites.   To take full advantage of the API, developers should familiarize themselves with the database by reading the database documentation available via links on [Data Type Documentation](https://fdc.nal.usda.gov/data-documentation.html). This documentation provides the detailed definitions and descriptions needed to understand the data elements referenced in the API documentation.      Additional details about the API including rate limits, access, and licensing are available on the [FDC website](https://fdc.nal.usda.gov/api-guide.html)

    The version of the OpenAPI document: 1.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class WweiaFoodCategory(BaseModel):
    """
    WweiaFoodCategory
    """
    wweia_food_category_code: Optional[StrictInt] = Field(None, alias="wweiaFoodCategoryCode")
    wweia_food_category_description: Optional[StrictStr] = Field(None, alias="wweiaFoodCategoryDescription")
    __properties = ["wweiaFoodCategoryCode", "wweiaFoodCategoryDescription"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> WweiaFoodCategory:
        """Create an instance of WweiaFoodCategory from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WweiaFoodCategory:
        """Create an instance of WweiaFoodCategory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WweiaFoodCategory.parse_obj(obj)

        _obj = WweiaFoodCategory.parse_obj({
            "wweia_food_category_code": obj.get("wweiaFoodCategoryCode"),
            "wweia_food_category_description": obj.get("wweiaFoodCategoryDescription")
        })
        return _obj


