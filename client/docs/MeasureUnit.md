# MeasureUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**abbreviation** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.measure_unit import MeasureUnit

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureUnit from a JSON string
measure_unit_instance = MeasureUnit.from_json(json)
# print the JSON string representation of the object
print MeasureUnit.to_json()

# convert the object into a dict
measure_unit_dict = measure_unit_instance.to_dict()
# create an instance of MeasureUnit from a dict
measure_unit_form_dict = measure_unit.from_dict(measure_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


