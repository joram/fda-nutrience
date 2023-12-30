# RetentionFactor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**code** | **int** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.retention_factor import RetentionFactor

# TODO update the JSON string below
json = "{}"
# create an instance of RetentionFactor from a JSON string
retention_factor_instance = RetentionFactor.from_json(json)
# print the JSON string representation of the object
print RetentionFactor.to_json()

# convert the object into a dict
retention_factor_dict = retention_factor_instance.to_dict()
# create an instance of RetentionFactor from a dict
retention_factor_form_dict = retention_factor.from_dict(retention_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


