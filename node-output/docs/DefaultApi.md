# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**news_events_post**](DefaultApi.md#news_events_post) | **POST** /newsEvents | Publish a news event

# **news_events_post**
> news_events_post(body)

Publish a news event

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.NewsEvent() # NewsEvent | 

try:
    # Publish a news event
    api_instance.news_events_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->news_events_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewsEvent**](NewsEvent.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

