# FoodNutrient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**amount** | **float** |  | [optional] 
**data_points** | **int** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**median** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**nutrient** | [**Nutrient**](Nutrient.md) |  | [optional] 
**food_nutrient_derivation** | [**FoodNutrientDerivation**](FoodNutrientDerivation.md) |  | [optional] 
**nutrient_analysis_details** | [**NutrientAnalysisDetails**](NutrientAnalysisDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.food_nutrient import FoodNutrient

# TODO update the JSON string below
json = "{}"
# create an instance of FoodNutrient from a JSON string
food_nutrient_instance = FoodNutrient.from_json(json)
# print the JSON string representation of the object
print FoodNutrient.to_json()

# convert the object into a dict
food_nutrient_dict = food_nutrient_instance.to_dict()
# create an instance of FoodNutrient from a dict
food_nutrient_form_dict = food_nutrient.from_dict(food_nutrient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


