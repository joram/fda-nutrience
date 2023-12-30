# SearchResultFood


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fdc_id** | **int** | Unique ID of the food. | 
**data_type** | **str** | The type of the food data. | [optional] 
**description** | **str** | The description of the food. | 
**food_code** | **str** | Any A unique ID identifying the food within FNDDS. | [optional] 
**food_nutrients** | [**List[AbridgedFoodNutrient]**](AbridgedFoodNutrient.md) |  | [optional] 
**publication_date** | **str** | Date the item was published to FDC. | [optional] 
**scientific_name** | **str** | The scientific name of the food. | [optional] 
**brand_owner** | **str** | Brand owner for the food. Only applies to Branded Foods. | [optional] 
**gtin_upc** | **str** | GTIN or UPC code identifying the food. Only applies to Branded Foods. | [optional] 
**ingredients** | **str** | The list of ingredients (as it appears on the product label). Only applies to Branded Foods. | [optional] 
**ndb_number** | **int** | Unique number assigned for foundation foods. Only applies to Foundation and SRLegacy Foods. | [optional] 
**additional_descriptions** | **str** | Any additional descriptions of the food. | [optional] 
**all_highlight_fields** | **str** | allHighlightFields | [optional] 
**score** | **float** | Relative score indicating how well the food matches the search criteria. | [optional] 

## Example

```python
from openapi_client.models.search_result_food import SearchResultFood

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultFood from a JSON string
search_result_food_instance = SearchResultFood.from_json(json)
# print the JSON string representation of the object
print SearchResultFood.to_json()

# convert the object into a dict
search_result_food_dict = search_result_food_instance.to_dict()
# create an instance of SearchResultFood from a dict
search_result_food_form_dict = search_result_food.from_dict(search_result_food_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


