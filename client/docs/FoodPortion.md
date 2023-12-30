# FoodPortion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**data_points** | **int** |  | [optional] 
**gram_weight** | **float** |  | [optional] 
**min_year_acquired** | **int** |  | [optional] 
**modifier** | **str** |  | [optional] 
**portion_description** | **str** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**measure_unit** | [**MeasureUnit**](MeasureUnit.md) |  | [optional] 

## Example

```python
from openapi_client.models.food_portion import FoodPortion

# TODO update the JSON string below
json = "{}"
# create an instance of FoodPortion from a JSON string
food_portion_instance = FoodPortion.from_json(json)
# print the JSON string representation of the object
print FoodPortion.to_json()

# convert the object into a dict
food_portion_dict = food_portion_instance.to_dict()
# create an instance of FoodPortion from a dict
food_portion_form_dict = food_portion.from_dict(food_portion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


