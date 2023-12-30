# FoodNutrientDerivation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**food_nutrient_source** | [**FoodNutrientSource**](FoodNutrientSource.md) |  | [optional] 

## Example

```python
from openapi_client.models.food_nutrient_derivation import FoodNutrientDerivation

# TODO update the JSON string below
json = "{}"
# create an instance of FoodNutrientDerivation from a JSON string
food_nutrient_derivation_instance = FoodNutrientDerivation.from_json(json)
# print the JSON string representation of the object
print FoodNutrientDerivation.to_json()

# convert the object into a dict
food_nutrient_derivation_dict = food_nutrient_derivation_instance.to_dict()
# create an instance of FoodNutrientDerivation from a dict
food_nutrient_derivation_form_dict = food_nutrient_derivation.from_dict(food_nutrient_derivation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


