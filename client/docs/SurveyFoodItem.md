# SurveyFoodItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fdc_id** | **int** |  | 
**datatype** | **str** |  | [optional] 
**description** | **str** |  | 
**end_date** | **str** |  | [optional] 
**food_class** | **str** |  | [optional] 
**food_code** | **str** |  | [optional] 
**publication_date** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**food_attributes** | [**List[FoodAttribute]**](FoodAttribute.md) |  | [optional] 
**food_portions** | [**List[FoodPortion]**](FoodPortion.md) |  | [optional] 
**input_foods** | [**List[InputFoodSurvey]**](InputFoodSurvey.md) |  | [optional] 
**wweia_food_category** | [**WweiaFoodCategory**](WweiaFoodCategory.md) |  | [optional] 

## Example

```python
from openapi_client.models.survey_food_item import SurveyFoodItem

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyFoodItem from a JSON string
survey_food_item_instance = SurveyFoodItem.from_json(json)
# print the JSON string representation of the object
print SurveyFoodItem.to_json()

# convert the object into a dict
survey_food_item_dict = survey_food_item_instance.to_dict()
# create an instance of SurveyFoodItem from a dict
survey_food_item_form_dict = survey_food_item.from_dict(survey_food_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


