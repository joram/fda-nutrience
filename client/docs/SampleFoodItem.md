# SampleFoodItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fdc_id** | **int** |  | 
**datatype** | **str** |  | [optional] 
**description** | **str** |  | 
**food_class** | **str** |  | [optional] 
**publication_date** | **str** |  | [optional] 
**food_attributes** | [**List[FoodCategory]**](FoodCategory.md) |  | [optional] 

## Example

```python
from openapi_client.models.sample_food_item import SampleFoodItem

# TODO update the JSON string below
json = "{}"
# create an instance of SampleFoodItem from a JSON string
sample_food_item_instance = SampleFoodItem.from_json(json)
# print the JSON string representation of the object
print SampleFoodItem.to_json()

# convert the object into a dict
sample_food_item_dict = sample_food_item_instance.to_dict()
# create an instance of SampleFoodItem from a dict
sample_food_item_form_dict = sample_food_item.from_dict(sample_food_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


