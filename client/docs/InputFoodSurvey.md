# InputFoodSurvey

applies to Survey (FNDDS). Not all inputFoods will have all fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**food_description** | **str** |  | [optional] 
**ingredient_code** | **int** |  | [optional] 
**ingredient_description** | **str** |  | [optional] 
**ingredient_weight** | **float** |  | [optional] 
**portion_code** | **str** |  | [optional] 
**portion_description** | **str** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**survey_flag** | **int** |  | [optional] 
**unit** | **str** |  | [optional] 
**input_food** | [**SurveyFoodItem**](SurveyFoodItem.md) |  | [optional] 
**retention_factor** | [**RetentionFactor**](RetentionFactor.md) |  | [optional] 

## Example

```python
from openapi_client.models.input_food_survey import InputFoodSurvey

# TODO update the JSON string below
json = "{}"
# create an instance of InputFoodSurvey from a JSON string
input_food_survey_instance = InputFoodSurvey.from_json(json)
# print the JSON string representation of the object
print InputFoodSurvey.to_json()

# convert the object into a dict
input_food_survey_dict = input_food_survey_instance.to_dict()
# create an instance of InputFoodSurvey from a dict
input_food_survey_form_dict = input_food_survey.from_dict(input_food_survey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


