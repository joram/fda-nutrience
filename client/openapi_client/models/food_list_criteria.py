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
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FoodListCriteria(BaseModel):
    """
    JSON for request body of 'list' POST request
    """ # noqa: E501
    data_type: Optional[Annotated[List[StrictStr], Field(min_length=1, max_length=4)]] = Field(default=None, description="Optional. Filter on a specific data type; specify one or more values in an array.", alias="dataType")
    page_size: Optional[Annotated[int, Field(le=200, strict=True, ge=1)]] = Field(default=None, description="Optional. Maximum number of results to return for the current page. Default is 50.", alias="pageSize")
    page_number: Optional[StrictInt] = Field(default=None, description="Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize)", alias="pageNumber")
    sort_by: Optional[StrictStr] = Field(default=None, description="Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and lowercaseDescription.keyword will be description in future releases.", alias="sortBy")
    sort_order: Optional[StrictStr] = Field(default=None, description="Optional. The sort direction for the results. Only applicable if sortBy is specified.", alias="sortOrder")
    __properties: ClassVar[List[str]] = ["dataType", "pageSize", "pageNumber", "sortBy", "sortOrder"]

    @field_validator('data_type')
    def data_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('Branded', 'Foundation', 'Survey (FNDDS)', 'SR Legacy'):
                raise ValueError("each list item must be one of ('Branded', 'Foundation', 'Survey (FNDDS)', 'SR Legacy')")
        return value

    @field_validator('sort_by')
    def sort_by_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('dataType.keyword', 'lowercaseDescription.keyword', 'fdcId', 'publishedDate'):
            raise ValueError("must be one of enum values ('dataType.keyword', 'lowercaseDescription.keyword', 'fdcId', 'publishedDate')")
        return value

    @field_validator('sort_order')
    def sort_order_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('asc', 'desc'):
            raise ValueError("must be one of enum values ('asc', 'desc')")
        return value

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
        """Create an instance of FoodListCriteria from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FoodListCriteria from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataType": obj.get("dataType"),
            "pageSize": obj.get("pageSize"),
            "pageNumber": obj.get("pageNumber"),
            "sortBy": obj.get("sortBy"),
            "sortOrder": obj.get("sortOrder")
        })
        return _obj


