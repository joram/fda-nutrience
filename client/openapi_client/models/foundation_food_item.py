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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from openapi_client.models.food_category import FoodCategory
from openapi_client.models.food_component import FoodComponent
from openapi_client.models.food_nutrient import FoodNutrient
from openapi_client.models.food_portion import FoodPortion
from openapi_client.models.input_food_foundation import InputFoodFoundation
from openapi_client.models.nutrient_conversion_factors import NutrientConversionFactors

class FoundationFoodItem(BaseModel):
    """
    FoundationFoodItem
    """
    fdc_id: StrictInt = Field(..., alias="fdcId")
    data_type: StrictStr = Field(..., alias="dataType")
    description: StrictStr = Field(...)
    food_class: Optional[StrictStr] = Field(None, alias="foodClass")
    foot_note: Optional[StrictStr] = Field(None, alias="footNote")
    is_historical_reference: Optional[StrictBool] = Field(None, alias="isHistoricalReference")
    ndb_number: Optional[StrictInt] = Field(None, alias="ndbNumber")
    publication_date: Optional[StrictStr] = Field(None, alias="publicationDate")
    scientific_name: Optional[StrictStr] = Field(None, alias="scientificName")
    food_category: Optional[FoodCategory] = Field(None, alias="foodCategory")
    food_components: Optional[conlist(FoodComponent)] = Field(None, alias="foodComponents")
    food_nutrients: Optional[conlist(FoodNutrient)] = Field(None, alias="foodNutrients")
    food_portions: Optional[conlist(FoodPortion)] = Field(None, alias="foodPortions")
    input_foods: Optional[conlist(InputFoodFoundation)] = Field(None, alias="inputFoods")
    nutrient_conversion_factors: Optional[conlist(NutrientConversionFactors)] = Field(None, alias="nutrientConversionFactors")
    __properties = ["fdcId", "dataType", "description", "foodClass", "footNote", "isHistoricalReference", "ndbNumber", "publicationDate", "scientificName", "foodCategory", "foodComponents", "foodNutrients", "foodPortions", "inputFoods", "nutrientConversionFactors"]

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
    def from_json(cls, json_str: str) -> FoundationFoodItem:
        """Create an instance of FoundationFoodItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of food_category
        if self.food_category:
            _dict['foodCategory'] = self.food_category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in food_components (list)
        _items = []
        if self.food_components:
            for _item in self.food_components:
                if _item:
                    _items.append(_item.to_dict())
            _dict['foodComponents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in food_nutrients (list)
        _items = []
        if self.food_nutrients:
            for _item in self.food_nutrients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['foodNutrients'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in food_portions (list)
        _items = []
        if self.food_portions:
            for _item in self.food_portions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['foodPortions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in input_foods (list)
        _items = []
        if self.input_foods:
            for _item in self.input_foods:
                if _item:
                    _items.append(_item.to_dict())
            _dict['inputFoods'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in nutrient_conversion_factors (list)
        _items = []
        if self.nutrient_conversion_factors:
            for _item in self.nutrient_conversion_factors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nutrientConversionFactors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FoundationFoodItem:
        """Create an instance of FoundationFoodItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FoundationFoodItem.parse_obj(obj)

        _obj = FoundationFoodItem.parse_obj({
            "fdc_id": obj.get("fdcId"),
            "data_type": obj.get("dataType"),
            "description": obj.get("description"),
            "food_class": obj.get("foodClass"),
            "foot_note": obj.get("footNote"),
            "is_historical_reference": obj.get("isHistoricalReference"),
            "ndb_number": obj.get("ndbNumber"),
            "publication_date": obj.get("publicationDate"),
            "scientific_name": obj.get("scientificName"),
            "food_category": FoodCategory.from_dict(obj.get("foodCategory")) if obj.get("foodCategory") is not None else None,
            "food_components": [FoodComponent.from_dict(_item) for _item in obj.get("foodComponents")] if obj.get("foodComponents") is not None else None,
            "food_nutrients": [FoodNutrient.from_dict(_item) for _item in obj.get("foodNutrients")] if obj.get("foodNutrients") is not None else None,
            "food_portions": [FoodPortion.from_dict(_item) for _item in obj.get("foodPortions")] if obj.get("foodPortions") is not None else None,
            "input_foods": [InputFoodFoundation.from_dict(_item) for _item in obj.get("inputFoods")] if obj.get("inputFoods") is not None else None,
            "nutrient_conversion_factors": [NutrientConversionFactors.from_dict(_item) for _item in obj.get("nutrientConversionFactors")] if obj.get("nutrientConversionFactors") is not None else None
        })
        return _obj


