# coding: utf-8

"""
    Food Data Central API

    The FoodData Central API provides REST access to FoodData Central (FDC). It is intended primarily to assist application developers wishing to incorporate nutrient data into their applications or websites.   To take full advantage of the API, developers should familiarize themselves with the database by reading the database documentation available via links on [Data Type Documentation](https://fdc.nal.usda.gov/data-documentation.html). This documentation provides the detailed definitions and descriptions needed to understand the data elements referenced in the API documentation.      Additional details about the API including rate limits, access, and licensing are available on the [FDC website](https://fdc.nal.usda.gov/api-guide.html)

    The version of the OpenAPI document: 1.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from openapi_client.models.abridged_food_item import AbridgedFoodItem
from openapi_client.models.branded_food_item import BrandedFoodItem
from openapi_client.models.foundation_food_item import FoundationFoodItem
from openapi_client.models.sr_legacy_food_item import SRLegacyFoodItem
from openapi_client.models.survey_food_item import SurveyFoodItem
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

INLINERESPONSE200_ONE_OF_SCHEMAS = ["AbridgedFoodItem", "BrandedFoodItem", "FoundationFoodItem", "SRLegacyFoodItem", "SurveyFoodItem"]

class InlineResponse200(BaseModel):
    """
    InlineResponse200
    """
    # data type: AbridgedFoodItem
    oneof_schema_1_validator: Optional[AbridgedFoodItem] = None
    # data type: BrandedFoodItem
    oneof_schema_2_validator: Optional[BrandedFoodItem] = None
    # data type: FoundationFoodItem
    oneof_schema_3_validator: Optional[FoundationFoodItem] = None
    # data type: SRLegacyFoodItem
    oneof_schema_4_validator: Optional[SRLegacyFoodItem] = None
    # data type: SurveyFoodItem
    oneof_schema_5_validator: Optional[SurveyFoodItem] = None
    actual_instance: Optional[Union[AbridgedFoodItem, BrandedFoodItem, FoundationFoodItem, SRLegacyFoodItem, SurveyFoodItem]] = None
    one_of_schemas: List[str] = Literal["AbridgedFoodItem", "BrandedFoodItem", "FoundationFoodItem", "SRLegacyFoodItem", "SurveyFoodItem"]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = InlineResponse200.model_construct()
        error_messages = []
        match = 0
        # validate data type: AbridgedFoodItem
        if not isinstance(v, AbridgedFoodItem):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AbridgedFoodItem`")
        else:
            match += 1
        # validate data type: BrandedFoodItem
        if not isinstance(v, BrandedFoodItem):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BrandedFoodItem`")
        else:
            match += 1
        # validate data type: FoundationFoodItem
        if not isinstance(v, FoundationFoodItem):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FoundationFoodItem`")
        else:
            match += 1
        # validate data type: SRLegacyFoodItem
        if not isinstance(v, SRLegacyFoodItem):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SRLegacyFoodItem`")
        else:
            match += 1
        # validate data type: SurveyFoodItem
        if not isinstance(v, SurveyFoodItem):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SurveyFoodItem`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in InlineResponse200 with oneOf schemas: AbridgedFoodItem, BrandedFoodItem, FoundationFoodItem, SRLegacyFoodItem, SurveyFoodItem. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in InlineResponse200 with oneOf schemas: AbridgedFoodItem, BrandedFoodItem, FoundationFoodItem, SRLegacyFoodItem, SurveyFoodItem. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into AbridgedFoodItem
        try:
            instance.actual_instance = AbridgedFoodItem.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BrandedFoodItem
        try:
            instance.actual_instance = BrandedFoodItem.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FoundationFoodItem
        try:
            instance.actual_instance = FoundationFoodItem.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SRLegacyFoodItem
        try:
            instance.actual_instance = SRLegacyFoodItem.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SurveyFoodItem
        try:
            instance.actual_instance = SurveyFoodItem.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into InlineResponse200 with oneOf schemas: AbridgedFoodItem, BrandedFoodItem, FoundationFoodItem, SRLegacyFoodItem, SurveyFoodItem. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into InlineResponse200 with oneOf schemas: AbridgedFoodItem, BrandedFoodItem, FoundationFoodItem, SRLegacyFoodItem, SurveyFoodItem. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


