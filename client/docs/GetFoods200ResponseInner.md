# GetFoods200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** |  | 
**description** | **str** |  | 
**fdc_id** | **int** |  | 
**food_nutrients** | [**List[FoodNutrient]**](FoodNutrient.md) |  | [optional] 
**publication_date** | **str** |  | [optional] 
**brand_owner** | **str** |  | [optional] 
**gtin_upc** | **str** |  | [optional] 
**ndb_number** | **int** |  | [optional] 
**food_code** | **str** |  | [optional] 
**available_date** | **str** |  | [optional] 
**data_source** | **str** |  | [optional] 
**food_class** | **str** |  | [optional] 
**household_serving_full_text** | **str** |  | [optional] 
**ingredients** | **str** |  | [optional] 
**modified_date** | **str** |  | [optional] 
**serving_size** | **int** |  | [optional] 
**serving_size_unit** | **str** |  | [optional] 
**preparation_state_code** | **str** |  | [optional] 
**branded_food_category** | **str** |  | [optional] 
**trade_channel** | **List[str]** |  | [optional] 
**gpc_class_code** | **int** |  | [optional] 
**food_update_log** | [**List[FoodUpdateLog]**](FoodUpdateLog.md) |  | [optional] 
**label_nutrients** | [**BrandedFoodItemLabelNutrients**](BrandedFoodItemLabelNutrients.md) |  | [optional] 
**foot_note** | **str** |  | [optional] 
**is_historical_reference** | **bool** |  | [optional] 
**scientific_name** | **str** |  | [optional] 
**food_category** | [**FoodCategory**](FoodCategory.md) |  | [optional] 
**food_components** | [**List[FoodComponent]**](FoodComponent.md) |  | [optional] 
**food_portions** | [**List[FoodPortion]**](FoodPortion.md) |  | [optional] 
**input_foods** | [**List[InputFoodSurvey]**](InputFoodSurvey.md) |  | [optional] 
**nutrient_conversion_factors** | [**List[NutrientConversionFactors]**](NutrientConversionFactors.md) |  | [optional] 
**datatype** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**food_attributes** | [**List[FoodAttribute]**](FoodAttribute.md) |  | [optional] 
**wweia_food_category** | [**WweiaFoodCategory**](WweiaFoodCategory.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_foods200_response_inner import GetFoods200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetFoods200ResponseInner from a JSON string
get_foods200_response_inner_instance = GetFoods200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetFoods200ResponseInner.to_json()

# convert the object into a dict
get_foods200_response_inner_dict = get_foods200_response_inner_instance.to_dict()
# create an instance of GetFoods200ResponseInner from a dict
get_foods200_response_inner_form_dict = get_foods200_response_inner.from_dict(get_foods200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


