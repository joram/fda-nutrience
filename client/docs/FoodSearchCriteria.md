# FoodSearchCriteria

A copy of the criteria that were used in the search.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Search terms to use in the search. The string may also include standard [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2) | [optional] 
**data_type** | **List[str]** | Optional. Filter on a specific data type; specify one or more values in an array. | [optional] 
**page_size** | **int** | Optional. Maximum number of results to return for the current page. Default is 50. | [optional] 
**page_number** | **int** | Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize) | [optional] 
**sort_by** | **str** | Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and description.keyword will be description in future releases. | [optional] 
**sort_order** | **str** | Optional. The sort direction for the results. Only applicable if sortBy is specified. | [optional] 
**brand_owner** | **str** | Optional. Filter results based on the brand owner of the food. Only applies to Branded Foods. | [optional] 
**trade_channel** | **List[str]** | Optional. Filter foods containing any of the specified trade channels. | [optional] 
**start_date** | **str** | Filter foods published on or after this date. Format: YYYY-MM-DD | [optional] 
**end_date** | **str** | Filter foods published on or before this date. Format: YYYY-MM-DD | [optional] 

## Example

```python
from openapi_client.models.food_search_criteria import FoodSearchCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of FoodSearchCriteria from a JSON string
food_search_criteria_instance = FoodSearchCriteria.from_json(json)
# print the JSON string representation of the object
print FoodSearchCriteria.to_json()

# convert the object into a dict
food_search_criteria_dict = food_search_criteria_instance.to_dict()
# create an instance of FoodSearchCriteria from a dict
food_search_criteria_form_dict = food_search_criteria.from_dict(food_search_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


