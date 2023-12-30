# openapi_client.FDCApi

All URIs are relative to *https://api.nal.usda.gov/fdc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_food**](FDCApi.md#get_food) | **GET** /v1/food/{fdcId} | Fetches details for one food item by FDC ID
[**get_foods**](FDCApi.md#get_foods) | **GET** /v1/foods | Fetches details for multiple food items using input FDC IDs
[**get_foods_list**](FDCApi.md#get_foods_list) | **GET** /v1/foods/list | Returns a paged list of foods, in the &#39;abridged&#39; format
[**get_foods_search**](FDCApi.md#get_foods_search) | **GET** /v1/foods/search | Returns a list of foods that matched search (query) keywords
[**get_json_spec**](FDCApi.md#get_json_spec) | **GET** /v1/json-spec | Returns this documentation in JSON format
[**get_yaml_spec**](FDCApi.md#get_yaml_spec) | **GET** /v1/yaml-spec | Returns this documentation in JSON format
[**post_foods**](FDCApi.md#post_foods) | **POST** /v1/foods | Fetches details for multiple food items using input FDC IDs
[**post_foods_list**](FDCApi.md#post_foods_list) | **POST** /v1/foods/list | Returns a paged list of foods, in the &#39;abridged&#39; format
[**post_foods_search**](FDCApi.md#post_foods_search) | **POST** /v1/foods/search | Returns a list of foods that matched search (query) keywords


# **get_food**
> InlineResponse200 get_food(fdc_id, format=format, nutrients=nutrients)

Fetches details for one food item by FDC ID

Retrieves a single food item by an FDC ID. Optional format and nutrients can be specified.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.inline_response200 import InlineResponse200
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nal.usda.gov/fdc
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.nal.usda.gov/fdc"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FDCApi(api_client)
    fdc_id = 'fdc_id_example' # str | FDC id of the food to retrieve
    format = 'format_example' # str | Optional. 'abridged' for an abridged set of elements, 'full' for all elements (default). (optional)
    nutrients = [[203,204,205]] # List[int] | Optional. List of up to 25 nutrient numbers. Only the nutrient information for the specified nutrients will be returned. Should be comma separated list (e.g. nutrients=203,204) or repeating parameters (e.g. nutrients=203&nutrients=204). If a food does not have any matching nutrients, the food will be returned with an empty foodNutrients element. (optional)

    try:
        # Fetches details for one food item by FDC ID
        api_response = api_instance.get_food(fdc_id, format=format, nutrients=nutrients)
        print("The response of FDCApi->get_food:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FDCApi->get_food: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fdc_id** | **str**| FDC id of the food to retrieve | 
 **format** | **str**| Optional. &#39;abridged&#39; for an abridged set of elements, &#39;full&#39; for all elements (default). | [optional] 
 **nutrients** | [**List[int]**](int.md)| Optional. List of up to 25 nutrient numbers. Only the nutrient information for the specified nutrients will be returned. Should be comma separated list (e.g. nutrients&#x3D;203,204) or repeating parameters (e.g. nutrients&#x3D;203&amp;nutrients&#x3D;204). If a food does not have any matching nutrients, the food will be returned with an empty foodNutrients element. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One food result. |  -  |
**400** | bad input parameter |  -  |
**404** | no results found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods**
> List[GetFoods200ResponseInner] get_foods(fdc_ids, format=format, nutrients=nutrients)

Fetches details for multiple food items using input FDC IDs

Retrieves a list of food items by a list of up to 20 FDC IDs. Optional format and nutrients can be specified. Invalid FDC ID's or ones that are not found are omitted and an empty set is returned if there are no matches.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.get_foods200_response_inner import GetFoods200ResponseInner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nal.usda.gov/fdc
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.nal.usda.gov/fdc"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FDCApi(api_client)
    fdc_ids = ['[534358,373052,616350]'] # List[str] | List of multiple FDC ID's. Should be comma separated list (e.g. fdcIds=534358,373052) or repeating parameters (e.g. fdcIds=534358&fdcIds=373052).
    format = 'format_example' # str | Optional. 'abridged' for an abridged set of elements, 'full' for all elements (default). (optional)
    nutrients = [[203,204,205]] # List[int] | Optional. List of up to 25 nutrient numbers. Only the nutrient information for the specified nutrients will be returned. Should be comma separated list (e.g. nutrients=203,204) or repeating parameters (e.g. nutrients=203&nutrients=204). If a food does not have any matching nutrients, the food will be returned with an empty foodNutrients element. (optional)

    try:
        # Fetches details for multiple food items using input FDC IDs
        api_response = api_instance.get_foods(fdc_ids, format=format, nutrients=nutrients)
        print("The response of FDCApi->get_foods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FDCApi->get_foods: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fdc_ids** | [**List[str]**](str.md)| List of multiple FDC ID&#39;s. Should be comma separated list (e.g. fdcIds&#x3D;534358,373052) or repeating parameters (e.g. fdcIds&#x3D;534358&amp;fdcIds&#x3D;373052). | 
 **format** | **str**| Optional. &#39;abridged&#39; for an abridged set of elements, &#39;full&#39; for all elements (default). | [optional] 
 **nutrients** | [**List[int]**](int.md)| Optional. List of up to 25 nutrient numbers. Only the nutrient information for the specified nutrients will be returned. Should be comma separated list (e.g. nutrients&#x3D;203,204) or repeating parameters (e.g. nutrients&#x3D;203&amp;nutrients&#x3D;204). If a food does not have any matching nutrients, the food will be returned with an empty foodNutrients element. | [optional] 

### Return type

[**List[GetFoods200ResponseInner]**](GetFoods200ResponseInner.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Food details matching specified FDC ID&#39;s. Invalid FDC ID&#39;s or ones that are not found are omitted. |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_list**
> List[AbridgedFoodItem] get_foods_list(data_type=data_type, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)

Returns a paged list of foods, in the 'abridged' format

Retrieves a paged list of foods. Use the pageNumber parameter to page through the entire result set.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.abridged_food_item import AbridgedFoodItem
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nal.usda.gov/fdc
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.nal.usda.gov/fdc"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FDCApi(api_client)
    data_type = ['[\"Foundation\",\"SR Legacy\"]'] # List[str] | Optional. Filter on a specific data type; specify one or more values in an array. (optional)
    page_size = 25 # int | Optional. Maximum number of results to return for the current page. Default is 50. (optional)
    page_number = 2 # int | Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize) (optional)
    sort_by = 'sort_by_example' # str | Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and lowercaseDescription.keyword will be description in future releases. (optional)
    sort_order = 'sort_order_example' # str | Optional. The sort direction for the results. Only applicable if sortBy is specified. (optional)

    try:
        # Returns a paged list of foods, in the 'abridged' format
        api_response = api_instance.get_foods_list(data_type=data_type, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order)
        print("The response of FDCApi->get_foods_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FDCApi->get_foods_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_type** | [**List[str]**](str.md)| Optional. Filter on a specific data type; specify one or more values in an array. | [optional] 
 **page_size** | **int**| Optional. Maximum number of results to return for the current page. Default is 50. | [optional] 
 **page_number** | **int**| Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize) | [optional] 
 **sort_by** | **str**| Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and lowercaseDescription.keyword will be description in future releases. | [optional] 
 **sort_order** | **str**| Optional. The sort direction for the results. Only applicable if sortBy is specified. | [optional] 

### Return type

[**List[AbridgedFoodItem]**](AbridgedFoodItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of foods for the requested page |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_search**
> SearchResult get_foods_search(query, data_type=data_type, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, brand_owner=brand_owner)

Returns a list of foods that matched search (query) keywords

Search for foods using keywords. Results can be filtered by dataType and there are options for result page sizes or sorting.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.search_result import SearchResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nal.usda.gov/fdc
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.nal.usda.gov/fdc"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FDCApi(api_client)
    query = 'cheddar cheese' # str | One or more search terms.  The string may include [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2)
    data_type = ['[\"Foundation\",\"SR Legacy\"]'] # List[str] | Optional. Filter on a specific data type; specify one or more values in an array. (optional)
    page_size = 25 # int | Optional. Maximum number of results to return for the current page. Default is 50. (optional)
    page_number = 2 # int | Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize) (optional)
    sort_by = 'dataType.keyword' # str | Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and lowercaseDescription.keyword will be description in future releases. (optional)
    sort_order = 'asc' # str | Optional. The sort direction for the results. Only applicable if sortBy is specified. (optional)
    brand_owner = 'Kar Nut Products Company' # str | Optional. Filter results based on the brand owner of the food. Only applies to Branded Foods (optional)

    try:
        # Returns a list of foods that matched search (query) keywords
        api_response = api_instance.get_foods_search(query, data_type=data_type, page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, brand_owner=brand_owner)
        print("The response of FDCApi->get_foods_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FDCApi->get_foods_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| One or more search terms.  The string may include [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2) | 
 **data_type** | [**List[str]**](str.md)| Optional. Filter on a specific data type; specify one or more values in an array. | [optional] 
 **page_size** | **int**| Optional. Maximum number of results to return for the current page. Default is 50. | [optional] 
 **page_number** | **int**| Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize) | [optional] 
 **sort_by** | **str**| Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and lowercaseDescription.keyword will be description in future releases. | [optional] 
 **sort_order** | **str**| Optional. The sort direction for the results. Only applicable if sortBy is specified. | [optional] 
 **brand_owner** | **str**| Optional. Filter results based on the brand owner of the food. Only applies to Branded Foods | [optional] 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of foods that matched search terms |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_json_spec**
> get_json_spec()

Returns this documentation in JSON format

The OpenAPI 3.0 specification for the FDC API rendered as JSON (JavaScript Object Notation)

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nal.usda.gov/fdc
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.nal.usda.gov/fdc"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FDCApi(api_client)

    try:
        # Returns this documentation in JSON format
        api_instance.get_json_spec()
    except Exception as e:
        print("Exception when calling FDCApi->get_json_spec: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | JSON rendering of OpenAPI 3.0 specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_yaml_spec**
> get_yaml_spec()

Returns this documentation in JSON format

The OpenAPI 3.0 specification for the FDC API rendered as YAML (YAML Ain't Markup Language)

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nal.usda.gov/fdc
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.nal.usda.gov/fdc"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FDCApi(api_client)

    try:
        # Returns this documentation in JSON format
        api_instance.get_yaml_spec()
    except Exception as e:
        print("Exception when calling FDCApi->get_yaml_spec: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | YAML rendering of OpenAPI 3.0 specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_foods**
> List[GetFoods200ResponseInner] post_foods(foods_criteria)

Fetches details for multiple food items using input FDC IDs

Retrieves a list of food items by a list of up to 20 FDC IDs. Optional format and nutrients can be specified. Invalid FDC ID's or ones that are not found are omitted and an empty set is returned if there are no matches.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.foods_criteria import FoodsCriteria
from openapi_client.models.get_foods200_response_inner import GetFoods200ResponseInner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nal.usda.gov/fdc
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.nal.usda.gov/fdc"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FDCApi(api_client)
    foods_criteria = openapi_client.FoodsCriteria() # FoodsCriteria | 

    try:
        # Fetches details for multiple food items using input FDC IDs
        api_response = api_instance.post_foods(foods_criteria)
        print("The response of FDCApi->post_foods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FDCApi->post_foods: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foods_criteria** | [**FoodsCriteria**](FoodsCriteria.md)|  | 

### Return type

[**List[GetFoods200ResponseInner]**](GetFoods200ResponseInner.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Food details matching specified FDC ID&#39;s. Invalid FDC ID&#39;s or ones that are not found are omitted. |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_foods_list**
> List[AbridgedFoodItem] post_foods_list(food_list_criteria)

Returns a paged list of foods, in the 'abridged' format

Retrieves a paged list of foods. Use the pageNumber parameter to page through the entire result set.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.abridged_food_item import AbridgedFoodItem
from openapi_client.models.food_list_criteria import FoodListCriteria
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nal.usda.gov/fdc
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.nal.usda.gov/fdc"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FDCApi(api_client)
    food_list_criteria = openapi_client.FoodListCriteria() # FoodListCriteria | 

    try:
        # Returns a paged list of foods, in the 'abridged' format
        api_response = api_instance.post_foods_list(food_list_criteria)
        print("The response of FDCApi->post_foods_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FDCApi->post_foods_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **food_list_criteria** | [**FoodListCriteria**](FoodListCriteria.md)|  | 

### Return type

[**List[AbridgedFoodItem]**](AbridgedFoodItem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of foods for the requested page |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_foods_search**
> SearchResult post_foods_search(food_search_criteria)

Returns a list of foods that matched search (query) keywords

Search for foods using keywords. Results can be filtered by dataType and there are options for result page sizes or sorting.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.food_search_criteria import FoodSearchCriteria
from openapi_client.models.search_result import SearchResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.nal.usda.gov/fdc
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.nal.usda.gov/fdc"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FDCApi(api_client)
    food_search_criteria = openapi_client.FoodSearchCriteria() # FoodSearchCriteria | The query string may also include standard [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2)

    try:
        # Returns a list of foods that matched search (query) keywords
        api_response = api_instance.post_foods_search(food_search_criteria)
        print("The response of FDCApi->post_foods_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FDCApi->post_foods_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **food_search_criteria** | [**FoodSearchCriteria**](FoodSearchCriteria.md)| The query string may also include standard [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2) | 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of foods that matched search terms |  -  |
**400** | bad input parameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

