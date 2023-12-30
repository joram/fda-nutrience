# FoodUpdateLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fdc_id** | **int** |  | [optional] 
**available_date** | **str** |  | [optional] 
**brand_owner** | **str** |  | [optional] 
**data_source** | **str** |  | [optional] 
**data_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**food_class** | **str** |  | [optional] 
**gtin_upc** | **str** |  | [optional] 
**household_serving_full_text** | **str** |  | [optional] 
**ingredients** | **str** |  | [optional] 
**modified_date** | **str** |  | [optional] 
**publication_date** | **str** |  | [optional] 
**serving_size** | **int** |  | [optional] 
**serving_size_unit** | **str** |  | [optional] 
**branded_food_category** | **str** |  | [optional] 
**changes** | **str** |  | [optional] 
**food_attributes** | [**List[FoodAttribute]**](FoodAttribute.md) |  | [optional] 

## Example

```python
from openapi_client.models.food_update_log import FoodUpdateLog

# TODO update the JSON string below
json = "{}"
# create an instance of FoodUpdateLog from a JSON string
food_update_log_instance = FoodUpdateLog.from_json(json)
# print the JSON string representation of the object
print FoodUpdateLog.to_json()

# convert the object into a dict
food_update_log_dict = food_update_log_instance.to_dict()
# create an instance of FoodUpdateLog from a dict
food_update_log_form_dict = food_update_log.from_dict(food_update_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


