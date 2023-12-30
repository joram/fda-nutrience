# FoodCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.food_category import FoodCategory

# TODO update the JSON string below
json = "{}"
# create an instance of FoodCategory from a JSON string
food_category_instance = FoodCategory.from_json(json)
# print the JSON string representation of the object
print FoodCategory.to_json()

# convert the object into a dict
food_category_dict = food_category_instance.to_dict()
# create an instance of FoodCategory from a dict
food_category_form_dict = food_category.from_dict(food_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


