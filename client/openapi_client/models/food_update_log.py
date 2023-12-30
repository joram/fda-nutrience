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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.food_attribute import FoodAttribute
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FoodUpdateLog(BaseModel):
    """
    FoodUpdateLog
    """ # noqa: E501
    fdc_id: Optional[StrictInt] = Field(default=None, alias="fdcId")
    available_date: Optional[StrictStr] = Field(default=None, alias="availableDate")
    brand_owner: Optional[StrictStr] = Field(default=None, alias="brandOwner")
    data_source: Optional[StrictStr] = Field(default=None, alias="dataSource")
    data_type: Optional[StrictStr] = Field(default=None, alias="dataType")
    description: Optional[StrictStr] = None
    food_class: Optional[StrictStr] = Field(default=None, alias="foodClass")
    gtin_upc: Optional[StrictStr] = Field(default=None, alias="gtinUpc")
    household_serving_full_text: Optional[StrictStr] = Field(default=None, alias="householdServingFullText")
    ingredients: Optional[StrictStr] = None
    modified_date: Optional[StrictStr] = Field(default=None, alias="modifiedDate")
    publication_date: Optional[StrictStr] = Field(default=None, alias="publicationDate")
    serving_size: Optional[StrictInt] = Field(default=None, alias="servingSize")
    serving_size_unit: Optional[StrictStr] = Field(default=None, alias="servingSizeUnit")
    branded_food_category: Optional[StrictStr] = Field(default=None, alias="brandedFoodCategory")
    changes: Optional[StrictStr] = None
    food_attributes: Optional[List[FoodAttribute]] = Field(default=None, alias="foodAttributes")
    __properties: ClassVar[List[str]] = ["fdcId", "availableDate", "brandOwner", "dataSource", "dataType", "description", "foodClass", "gtinUpc", "householdServingFullText", "ingredients", "modifiedDate", "publicationDate", "servingSize", "servingSizeUnit", "brandedFoodCategory", "changes", "foodAttributes"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FoodUpdateLog from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in food_attributes (list)
        _items = []
        if self.food_attributes:
            for _item in self.food_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['foodAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FoodUpdateLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fdcId": obj.get("fdcId"),
            "availableDate": obj.get("availableDate"),
            "brandOwner": obj.get("brandOwner"),
            "dataSource": obj.get("dataSource"),
            "dataType": obj.get("dataType"),
            "description": obj.get("description"),
            "foodClass": obj.get("foodClass"),
            "gtinUpc": obj.get("gtinUpc"),
            "householdServingFullText": obj.get("householdServingFullText"),
            "ingredients": obj.get("ingredients"),
            "modifiedDate": obj.get("modifiedDate"),
            "publicationDate": obj.get("publicationDate"),
            "servingSize": obj.get("servingSize"),
            "servingSizeUnit": obj.get("servingSizeUnit"),
            "brandedFoodCategory": obj.get("brandedFoodCategory"),
            "changes": obj.get("changes"),
            "foodAttributes": [FoodAttribute.from_dict(_item) for _item in obj.get("foodAttributes")] if obj.get("foodAttributes") is not None else None
        })
        return _obj


