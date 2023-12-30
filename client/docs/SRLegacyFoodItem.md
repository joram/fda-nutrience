# SRLegacyFoodItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fdc_id** | **int** |  | 
**data_type** | **str** |  | 
**description** | **str** |  | 
**food_class** | **str** |  | [optional] 
**is_historical_reference** | **bool** |  | [optional] 
**ndb_number** | **int** |  | [optional] 
**publication_date** | **str** |  | [optional] 
**scientific_name** | **str** |  | [optional] 
**food_category** | [**FoodCategory**](FoodCategory.md) |  | [optional] 
**food_nutrients** | [**List[FoodNutrient]**](FoodNutrient.md) |  | [optional] 
**nutrient_conversion_factors** | [**List[NutrientConversionFactors]**](NutrientConversionFactors.md) |  | [optional] 

## Example

```python
from openapi_client.models.sr_legacy_food_item import SRLegacyFoodItem

# TODO update the JSON string below
json = "{}"
# create an instance of SRLegacyFoodItem from a JSON string
sr_legacy_food_item_instance = SRLegacyFoodItem.from_json(json)
# print the JSON string representation of the object
print SRLegacyFoodItem.to_json()

# convert the object into a dict
sr_legacy_food_item_dict = sr_legacy_food_item_instance.to_dict()
# create an instance of SRLegacyFoodItem from a dict
sr_legacy_food_item_form_dict = sr_legacy_food_item.from_dict(sr_legacy_food_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


