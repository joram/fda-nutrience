# WweiaFoodCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wweia_food_category_code** | **int** |  | [optional] 
**wweia_food_category_description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.wweia_food_category import WweiaFoodCategory

# TODO update the JSON string below
json = "{}"
# create an instance of WweiaFoodCategory from a JSON string
wweia_food_category_instance = WweiaFoodCategory.from_json(json)
# print the JSON string representation of the object
print WweiaFoodCategory.to_json()

# convert the object into a dict
wweia_food_category_dict = wweia_food_category_instance.to_dict()
# create an instance of WweiaFoodCategory from a dict
wweia_food_category_form_dict = wweia_food_category.from_dict(wweia_food_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


