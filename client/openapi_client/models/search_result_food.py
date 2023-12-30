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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.abridged_food_nutrient import AbridgedFoodNutrient
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SearchResultFood(BaseModel):
    """
    SearchResultFood
    """ # noqa: E501
    fdc_id: StrictInt = Field(description="Unique ID of the food.", alias="fdcId")
    data_type: Optional[StrictStr] = Field(default=None, description="The type of the food data.", alias="dataType")
    description: StrictStr = Field(description="The description of the food.")
    food_code: Optional[StrictStr] = Field(default=None, description="Any A unique ID identifying the food within FNDDS.", alias="foodCode")
    food_nutrients: Optional[List[AbridgedFoodNutrient]] = Field(default=None, alias="foodNutrients")
    publication_date: Optional[StrictStr] = Field(default=None, description="Date the item was published to FDC.", alias="publicationDate")
    scientific_name: Optional[StrictStr] = Field(default=None, description="The scientific name of the food.", alias="scientificName")
    brand_owner: Optional[StrictStr] = Field(default=None, description="Brand owner for the food. Only applies to Branded Foods.", alias="brandOwner")
    gtin_upc: Optional[StrictStr] = Field(default=None, description="GTIN or UPC code identifying the food. Only applies to Branded Foods.", alias="gtinUpc")
    ingredients: Optional[StrictStr] = Field(default=None, description="The list of ingredients (as it appears on the product label). Only applies to Branded Foods.")
    ndb_number: Optional[StrictInt] = Field(default=None, description="Unique number assigned for foundation foods. Only applies to Foundation and SRLegacy Foods.", alias="ndbNumber")
    additional_descriptions: Optional[StrictStr] = Field(default=None, description="Any additional descriptions of the food.", alias="additionalDescriptions")
    all_highlight_fields: Optional[StrictStr] = Field(default=None, description="allHighlightFields", alias="allHighlightFields")
    score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Relative score indicating how well the food matches the search criteria.")
    __properties: ClassVar[List[str]] = ["fdcId", "dataType", "description", "foodCode", "foodNutrients", "publicationDate", "scientificName", "brandOwner", "gtinUpc", "ingredients", "ndbNumber", "additionalDescriptions", "allHighlightFields", "score"]

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
        """Create an instance of SearchResultFood from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in food_nutrients (list)
        _items = []
        if self.food_nutrients:
            for _item in self.food_nutrients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['foodNutrients'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SearchResultFood from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fdcId": obj.get("fdcId"),
            "dataType": obj.get("dataType"),
            "description": obj.get("description"),
            "foodCode": obj.get("foodCode"),
            "foodNutrients": [AbridgedFoodNutrient.from_dict(_item) for _item in obj.get("foodNutrients")] if obj.get("foodNutrients") is not None else None,
            "publicationDate": obj.get("publicationDate"),
            "scientificName": obj.get("scientificName"),
            "brandOwner": obj.get("brandOwner"),
            "gtinUpc": obj.get("gtinUpc"),
            "ingredients": obj.get("ingredients"),
            "ndbNumber": obj.get("ndbNumber"),
            "additionalDescriptions": obj.get("additionalDescriptions"),
            "allHighlightFields": obj.get("allHighlightFields"),
            "score": obj.get("score")
        })
        return _obj

