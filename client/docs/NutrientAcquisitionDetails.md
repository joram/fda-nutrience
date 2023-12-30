# NutrientAcquisitionDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_unit_id** | **int** |  | [optional] 
**purchase_date** | **str** |  | [optional] 
**store_city** | **str** |  | [optional] 
**store_state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.nutrient_acquisition_details import NutrientAcquisitionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NutrientAcquisitionDetails from a JSON string
nutrient_acquisition_details_instance = NutrientAcquisitionDetails.from_json(json)
# print the JSON string representation of the object
print NutrientAcquisitionDetails.to_json()

# convert the object into a dict
nutrient_acquisition_details_dict = nutrient_acquisition_details_instance.to_dict()
# create an instance of NutrientAcquisitionDetails from a dict
nutrient_acquisition_details_form_dict = nutrient_acquisition_details.from_dict(nutrient_acquisition_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


