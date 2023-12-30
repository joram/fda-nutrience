# FoodAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**value** | **str** |  | [optional] 
**food_attribute_type** | [**FoodAttributeFoodAttributeType**](FoodAttributeFoodAttributeType.md) |  | [optional] 

## Example

```python
from openapi_client.models.food_attribute import FoodAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of FoodAttribute from a JSON string
food_attribute_instance = FoodAttribute.from_json(json)
# print the JSON string representation of the object
print FoodAttribute.to_json()

# convert the object into a dict
food_attribute_dict = food_attribute_instance.to_dict()
# create an instance of FoodAttribute from a dict
food_attribute_form_dict = food_attribute.from_dict(food_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


