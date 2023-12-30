# BrandedFoodItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fdc_id** | **int** |  | 
**available_date** | **str** |  | [optional] 
**brand_owner** | **str** |  | [optional] 
**data_source** | **str** |  | [optional] 
**data_type** | **str** |  | 
**description** | **str** |  | 
**food_class** | **str** |  | [optional] 
**gtin_upc** | **str** |  | [optional] 
**household_serving_full_text** | **str** |  | [optional] 
**ingredients** | **str** |  | [optional] 
**modified_date** | **str** |  | [optional] 
**publication_date** | **str** |  | [optional] 
**serving_size** | **int** |  | [optional] 
**serving_size_unit** | **str** |  | [optional] 
**preparation_state_code** | **str** |  | [optional] 
**branded_food_category** | **str** |  | [optional] 
**trade_channel** | **List[str]** |  | [optional] 
**gpc_class_code** | **int** |  | [optional] 
**food_nutrients** | [**List[FoodNutrient]**](FoodNutrient.md) |  | [optional] 
**food_update_log** | [**List[FoodUpdateLog]**](FoodUpdateLog.md) |  | [optional] 
**label_nutrients** | [**BrandedFoodItemLabelNutrients**](BrandedFoodItemLabelNutrients.md) |  | [optional] 

## Example

```python
from openapi_client.models.branded_food_item import BrandedFoodItem

# TODO update the JSON string below
json = "{}"
# create an instance of BrandedFoodItem from a JSON string
branded_food_item_instance = BrandedFoodItem.from_json(json)
# print the JSON string representation of the object
print BrandedFoodItem.to_json()

# convert the object into a dict
branded_food_item_dict = branded_food_item_instance.to_dict()
# create an instance of BrandedFoodItem from a dict
branded_food_item_form_dict = branded_food_item.from_dict(branded_food_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


