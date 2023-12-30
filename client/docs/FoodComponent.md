# FoodComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**data_points** | **int** |  | [optional] 
**gram_weight** | **float** |  | [optional] 
**is_refuse** | **bool** |  | [optional] 
**min_year_acquired** | **int** |  | [optional] 
**percent_weight** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.food_component import FoodComponent

# TODO update the JSON string below
json = "{}"
# create an instance of FoodComponent from a JSON string
food_component_instance = FoodComponent.from_json(json)
# print the JSON string representation of the object
print FoodComponent.to_json()

# convert the object into a dict
food_component_dict = food_component_instance.to_dict()
# create an instance of FoodComponent from a dict
food_component_form_dict = food_component.from_dict(food_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


