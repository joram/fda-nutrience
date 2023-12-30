# AbridgedFoodNutrient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**unit_name** | **str** |  | [optional] 
**derivation_code** | **str** |  | [optional] 
**derivation_description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.abridged_food_nutrient import AbridgedFoodNutrient

# TODO update the JSON string below
json = "{}"
# create an instance of AbridgedFoodNutrient from a JSON string
abridged_food_nutrient_instance = AbridgedFoodNutrient.from_json(json)
# print the JSON string representation of the object
print AbridgedFoodNutrient.to_json()

# convert the object into a dict
abridged_food_nutrient_dict = abridged_food_nutrient_instance.to_dict()
# create an instance of AbridgedFoodNutrient from a dict
abridged_food_nutrient_form_dict = abridged_food_nutrient.from_dict(abridged_food_nutrient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


