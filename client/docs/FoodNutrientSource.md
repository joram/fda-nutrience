# FoodNutrientSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.food_nutrient_source import FoodNutrientSource

# TODO update the JSON string below
json = "{}"
# create an instance of FoodNutrientSource from a JSON string
food_nutrient_source_instance = FoodNutrientSource.from_json(json)
# print the JSON string representation of the object
print FoodNutrientSource.to_json()

# convert the object into a dict
food_nutrient_source_dict = food_nutrient_source_instance.to_dict()
# create an instance of FoodNutrientSource from a dict
food_nutrient_source_form_dict = food_nutrient_source.from_dict(food_nutrient_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


