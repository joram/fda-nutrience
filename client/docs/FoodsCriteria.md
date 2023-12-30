# FoodsCriteria

JSON for request body of 'foods' POST request. Retrieves a list of food items by a list of up to 20 FDC IDs. Optional format and nutrients can be specified. Invalid FDC ID's or ones that are not found are omitted and an empty set is returned if there are no matches.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fdc_ids** | **List[int]** | List of multiple FDC ID&#39;s | [optional] 
**format** | **str** | Optional. &#39;abridged&#39; for an abridged set of elements, &#39;full&#39; for all elements (default). | [optional] 
**nutrients** | **List[int]** | Optional. List of up to 25 nutrient numbers. Only the nutrient information for the specified nutrients will be returned.  If a food does not have any matching nutrients, the food will be returned with an empty foodNutrients element. | [optional] 

## Example

```python
from openapi_client.models.foods_criteria import FoodsCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of FoodsCriteria from a JSON string
foods_criteria_instance = FoodsCriteria.from_json(json)
# print the JSON string representation of the object
print FoodsCriteria.to_json()

# convert the object into a dict
foods_criteria_dict = foods_criteria_instance.to_dict()
# create an instance of FoodsCriteria from a dict
foods_criteria_form_dict = foods_criteria.from_dict(foods_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


