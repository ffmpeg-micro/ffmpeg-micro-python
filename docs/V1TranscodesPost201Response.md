# V1TranscodesPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** | New jobs always start as &#x60;pending&#x60; | 
**input_url** | **str** | First input URL (echo) | [optional] 
**output_format** | **str** |  | [optional] 
**download_token** | **str** | Token for anonymous \&quot;Try It\&quot; downloads | [optional] 
**metadata** | [**V1TranscodesPost201ResponseMetadata**](V1TranscodesPost201ResponseMetadata.md) |  | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_transcodes_post201_response import V1TranscodesPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1TranscodesPost201Response from a JSON string
v1_transcodes_post201_response_instance = V1TranscodesPost201Response.from_json(json)
# print the JSON string representation of the object
print(V1TranscodesPost201Response.to_json())

# convert the object into a dict
v1_transcodes_post201_response_dict = v1_transcodes_post201_response_instance.to_dict()
# create an instance of V1TranscodesPost201Response from a dict
v1_transcodes_post201_response_from_dict = V1TranscodesPost201Response.from_dict(v1_transcodes_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


