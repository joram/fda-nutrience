# Nutrient

a food nutrient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**number** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**rank** | **int** |  | [optional] 
**unit_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.nutrient import Nutrient

# TODO update the JSON string below
json = "{}"
# create an instance of Nutrient from a JSON string
nutrient_instance = Nutrient.from_json(json)
# print the JSON string representation of the object
print Nutrient.to_json()

# convert the object into a dict
nutrient_dict = nutrient_instance.to_dict()
# create an instance of Nutrient from a dict
nutrient_form_dict = nutrient.from_dict(nutrient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


