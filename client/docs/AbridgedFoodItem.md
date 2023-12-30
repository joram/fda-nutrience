# AbridgedFoodItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  | 
**description** | **str** |  | 
**fdc_id** | **int** |  | 
**food_nutrients** | [**List[AbridgedFoodNutrient]**](AbridgedFoodNutrient.md) |  | [optional] 
**publication_date** | **str** |  | [optional] 
**brand_owner** | **str** | only applies to Branded Foods | [optional] 
**gtin_upc** | **str** | only applies to Branded Foods | [optional] 
**ndb_number** | **int** | only applies to Foundation and SRLegacy Foods | [optional] 
**food_code** | **str** | only applies to Survey Foods | [optional] 

## Example

```python
from openapi_client.models.abridged_food_item import AbridgedFoodItem

# TODO update the JSON string below
json = "{}"
# create an instance of AbridgedFoodItem from a JSON string
abridged_food_item_instance = AbridgedFoodItem.from_json(json)
# print the JSON string representation of the object
print AbridgedFoodItem.to_json()

# convert the object into a dict
abridged_food_item_dict = abridged_food_item_instance.to_dict()
# create an instance of AbridgedFoodItem from a dict
abridged_food_item_form_dict = abridged_food_item.from_dict(abridged_food_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


