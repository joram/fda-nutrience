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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from openapi_client.models.nutrient_acquisition_details import NutrientAcquisitionDetails

class NutrientAnalysisDetails(BaseModel):
    """
    NutrientAnalysisDetails
    """
    sub_sample_id: Optional[StrictInt] = Field(None, alias="subSampleId")
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    nutrient_id: Optional[StrictInt] = Field(None, alias="nutrientId")
    lab_method_description: Optional[StrictStr] = Field(None, alias="labMethodDescription")
    lab_method_original_description: Optional[StrictStr] = Field(None, alias="labMethodOriginalDescription")
    lab_method_link: Optional[StrictStr] = Field(None, alias="labMethodLink")
    lab_method_technique: Optional[StrictStr] = Field(None, alias="labMethodTechnique")
    nutrient_acquisition_details: Optional[conlist(NutrientAcquisitionDetails)] = Field(None, alias="nutrientAcquisitionDetails")
    __properties = ["subSampleId", "amount", "nutrientId", "labMethodDescription", "labMethodOriginalDescription", "labMethodLink", "labMethodTechnique", "nutrientAcquisitionDetails"]

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
    def from_json(cls, json_str: str) -> NutrientAnalysisDetails:
        """Create an instance of NutrientAnalysisDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in nutrient_acquisition_details (list)
        _items = []
        if self.nutrient_acquisition_details:
            for _item in self.nutrient_acquisition_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['nutrientAcquisitionDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NutrientAnalysisDetails:
        """Create an instance of NutrientAnalysisDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NutrientAnalysisDetails.parse_obj(obj)

        _obj = NutrientAnalysisDetails.parse_obj({
            "sub_sample_id": obj.get("subSampleId"),
            "amount": obj.get("amount"),
            "nutrient_id": obj.get("nutrientId"),
            "lab_method_description": obj.get("labMethodDescription"),
            "lab_method_original_description": obj.get("labMethodOriginalDescription"),
            "lab_method_link": obj.get("labMethodLink"),
            "lab_method_technique": obj.get("labMethodTechnique"),
            "nutrient_acquisition_details": [NutrientAcquisitionDetails.from_dict(_item) for _item in obj.get("nutrientAcquisitionDetails")] if obj.get("nutrientAcquisitionDetails") is not None else None
        })
        return _obj


