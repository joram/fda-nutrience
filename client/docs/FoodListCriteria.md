# FoodListCriteria

JSON for request body of 'list' POST request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **List[str]** | Optional. Filter on a specific data type; specify one or more values in an array. | [optional] 
**page_size** | **int** | Optional. Maximum number of results to return for the current page. Default is 50. | [optional] 
**page_number** | **int** | Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize) | [optional] 
**sort_by** | **str** | Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and lowercaseDescription.keyword will be description in future releases. | [optional] 
**sort_order** | **str** | Optional. The sort direction for the results. Only applicable if sortBy is specified. | [optional] 

## Example

```python
from openapi_client.models.food_list_criteria import FoodListCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of FoodListCriteria from a JSON string
food_list_criteria_instance = FoodListCriteria.from_json(json)
# print the JSON string representation of the object
print FoodListCriteria.to_json()

# convert the object into a dict
food_list_criteria_dict = food_list_criteria_instance.to_dict()
# create an instance of FoodListCriteria from a dict
food_list_criteria_form_dict = food_list_criteria.from_dict(food_list_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


