# SearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**food_search_criteria** | [**FoodSearchCriteria**](FoodSearchCriteria.md) |  | [optional] 
**total_hits** | **int** | The total number of foods found matching the search criteria. | [optional] 
**current_page** | **int** | The current page of results being returned. | [optional] 
**total_pages** | **int** | The total number of pages found matching the search criteria. | [optional] 
**foods** | [**List[SearchResultFood]**](SearchResultFood.md) | The list of foods found matching the search criteria. See Food Fields below. | [optional] 

## Example

```python
from openapi_client.models.search_result import SearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResult from a JSON string
search_result_instance = SearchResult.from_json(json)
# print the JSON string representation of the object
print SearchResult.to_json()

# convert the object into a dict
search_result_dict = search_result_instance.to_dict()
# create an instance of SearchResult from a dict
search_result_form_dict = search_result.from_dict(search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


