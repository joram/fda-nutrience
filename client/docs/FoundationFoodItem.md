# FoundationFoodItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fdc_id** | **int** |  | 
**data_type** | **str** |  | 
**description** | **str** |  | 
**food_class** | **str** |  | [optional] 
**foot_note** | **str** |  | [optional] 
**is_historical_reference** | **bool** |  | [optional] 
**ndb_number** | **int** |  | [optional] 
**publication_date** | **str** |  | [optional] 
**scientific_name** | **str** |  | [optional] 
**food_category** | [**FoodCategory**](FoodCategory.md) |  | [optional] 
**food_components** | [**List[FoodComponent]**](FoodComponent.md) |  | [optional] 
**food_nutrients** | [**List[FoodNutrient]**](FoodNutrient.md) |  | [optional] 
**food_portions** | [**List[FoodPortion]**](FoodPortion.md) |  | [optional] 
**input_foods** | [**List[InputFoodFoundation]**](InputFoodFoundation.md) |  | [optional] 
**nutrient_conversion_factors** | [**List[NutrientConversionFactors]**](NutrientConversionFactors.md) |  | [optional] 

## Example

```python
from openapi_client.models.foundation_food_item import FoundationFoodItem

# TODO update the JSON string below
json = "{}"
# create an instance of FoundationFoodItem from a JSON string
foundation_food_item_instance = FoundationFoodItem.from_json(json)
# print the JSON string representation of the object
print FoundationFoodItem.to_json()

# convert the object into a dict
foundation_food_item_dict = foundation_food_item_instance.to_dict()
# create an instance of FoundationFoodItem from a dict
foundation_food_item_form_dict = foundation_food_item.from_dict(foundation_food_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


