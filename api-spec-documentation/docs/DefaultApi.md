# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_id_delete**](DefaultApi.md#events_id_delete) | **DELETE** /events/{id} | Delete Event
[**events_id_get**](DefaultApi.md#events_id_get) | **GET** /events/{id} | Select Event
[**events_id_put**](DefaultApi.md#events_id_put) | **PUT** /events/{id} | Update Event
[**events_list_get**](DefaultApi.md#events_list_get) | **GET** /events/list | List Events
[**events_post**](DefaultApi.md#events_post) | **POST** /events | Create Event
[**events_share_event_post**](DefaultApi.md#events_share_event_post) | **POST** /events/share_event | Share Event

# **events_id_delete**
> events_id_delete(id)

Delete Event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | ID of the item to fetch

try:
    # Delete Event
    api_instance.events_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->events_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the item to fetch | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_id_get**
> Event events_id_get(id)

Select Event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | ID of the item to fetch

try:
    # Select Event
    api_response = api_instance.events_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->events_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the item to fetch | 

### Return type

[**Event**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_id_put**
> events_id_put(body, id)

Update Event

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
id = 'id_example' # str | ID of the item to fetch

try:
    # Update Event
    api_instance.events_id_put(body, id)
except ApiException as e:
    print("Exception when calling DefaultApi->events_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Event**](Event.md)|  | 
 **id** | **str**| ID of the item to fetch | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_list_get**
> list[Event] events_list_get()

List Events

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # List Events
    api_response = api_instance.events_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->events_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_post**
> Inlineresponse201 events_post(body)

Create Event

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
    # Create Event
    api_response = api_instance.events_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->events_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Event**](Event.md)|  | 

### Return type

[**Inlineresponse201**](Inlineresponse201.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_share_event_post**
> events_share_event_post(id, user_id, share)

Share Event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Event id
user_id = 'All' # str | The id of the user to share with - specific user or can take All to grant every one access (default to All)
share = true # bool | Indicates to add a share or remove a share (default to true)

try:
    # Share Event
    api_instance.events_share_event_post(id, user_id, share)
except ApiException as e:
    print("Exception when calling DefaultApi->events_share_event_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Event id | 
 **user_id** | **str**| The id of the user to share with - specific user or can take All to grant every one access | [default to All]
 **share** | **bool**| Indicates to add a share or remove a share | [default to true]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

