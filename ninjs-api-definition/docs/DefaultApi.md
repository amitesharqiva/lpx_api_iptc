# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_metadata_uri_get**](DefaultApi.md#events_metadata_uri_get) | **GET** /events/metadata/{uri} | Get event metadata
[**events_post**](DefaultApi.md#events_post) | **POST** /events | Publish an event
[**events_retrive_uri_get**](DefaultApi.md#events_retrive_uri_get) | **GET** /events/retrive/{uri} | Retrive an event

# **events_metadata_uri_get**
> RenditionType events_metadata_uri_get(uri)

Get event metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
uri = 'uri_example' # str | 

try:
    # Get event metadata
    api_response = api_instance.events_metadata_uri_get(uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->events_metadata_uri_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**|  | 

### Return type

[**RenditionType**](RenditionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_post**
> events_post(body)

Publish an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Event() # Event | 

try:
    # Publish an event
    api_instance.events_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->events_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Event**](Event.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_retrive_uri_get**
> Event events_retrive_uri_get(uri)

Retrive an event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
uri = 'uri_example' # str | 

try:
    # Retrive an event
    api_response = api_instance.events_retrive_uri_get(uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->events_retrive_uri_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**|  | 

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

