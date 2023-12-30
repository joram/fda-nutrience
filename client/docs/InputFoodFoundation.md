# InputFoodFoundation

applies to Foundation foods. Not all inputFoods will have all fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**food_description** | **str** |  | [optional] 
**input_food** | [**SampleFoodItem**](SampleFoodItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.input_food_foundation import InputFoodFoundation

# TODO update the JSON string below
json = "{}"
# create an instance of InputFoodFoundation from a JSON string
input_food_foundation_instance = InputFoodFoundation.from_json(json)
# print the JSON string representation of the object
print InputFoodFoundation.to_json()

# convert the object into a dict
input_food_foundation_dict = input_food_foundation_instance.to_dict()
# create an instance of InputFoodFoundation from a dict
input_food_foundation_form_dict = input_food_foundation.from_dict(input_food_foundation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


