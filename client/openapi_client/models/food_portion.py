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
from openapi_client.models.measure_unit import MeasureUnit
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FoodPortion(BaseModel):
    """
    FoodPortion
    """ # noqa: E501
    id: Optional[StrictInt] = None
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    data_points: Optional[StrictInt] = Field(default=None, alias="dataPoints")
    gram_weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gramWeight")
    min_year_acquired: Optional[StrictInt] = Field(default=None, alias="minYearAcquired")
    modifier: Optional[StrictStr] = None
    portion_description: Optional[StrictStr] = Field(default=None, alias="portionDescription")
    sequence_number: Optional[StrictInt] = Field(default=None, alias="sequenceNumber")
    measure_unit: Optional[MeasureUnit] = Field(default=None, alias="measureUnit")
    __properties: ClassVar[List[str]] = ["id", "amount", "dataPoints", "gramWeight", "minYearAcquired", "modifier", "portionDescription", "sequenceNumber", "measureUnit"]

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
        """Create an instance of FoodPortion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of measure_unit
        if self.measure_unit:
            _dict['measureUnit'] = self.measure_unit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FoodPortion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "amount": obj.get("amount"),
            "dataPoints": obj.get("dataPoints"),
            "gramWeight": obj.get("gramWeight"),
            "minYearAcquired": obj.get("minYearAcquired"),
            "modifier": obj.get("modifier"),
            "portionDescription": obj.get("portionDescription"),
            "sequenceNumber": obj.get("sequenceNumber"),
            "measureUnit": MeasureUnit.from_dict(obj.get("measureUnit")) if obj.get("measureUnit") is not None else None
        })
        return _obj


