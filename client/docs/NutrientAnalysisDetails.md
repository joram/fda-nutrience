# NutrientAnalysisDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_sample_id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**nutrient_id** | **int** |  | [optional] 
**lab_method_description** | **str** |  | [optional] 
**lab_method_original_description** | **str** |  | [optional] 
**lab_method_link** | **str** |  | [optional] 
**lab_method_technique** | **str** |  | [optional] 
**nutrient_acquisition_details** | [**List[NutrientAcquisitionDetails]**](NutrientAcquisitionDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.nutrient_analysis_details import NutrientAnalysisDetails

# TODO update the JSON string below
json = "{}"
# create an instance of NutrientAnalysisDetails from a JSON string
nutrient_analysis_details_instance = NutrientAnalysisDetails.from_json(json)
# print the JSON string representation of the object
print NutrientAnalysisDetails.to_json()

# convert the object into a dict
nutrient_analysis_details_dict = nutrient_analysis_details_instance.to_dict()
# create an instance of NutrientAnalysisDetails from a dict
nutrient_analysis_details_form_dict = nutrient_analysis_details.from_dict(nutrient_analysis_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


