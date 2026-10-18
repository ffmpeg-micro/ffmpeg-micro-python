# V1TranscodesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Transcode]**](Transcode.md) |  | [optional] 
**page** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_transcodes_get200_response import V1TranscodesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1TranscodesGet200Response from a JSON string
v1_transcodes_get200_response_instance = V1TranscodesGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1TranscodesGet200Response.to_json())

# convert the object into a dict
v1_transcodes_get200_response_dict = v1_transcodes_get200_response_instance.to_dict()
# create an instance of V1TranscodesGet200Response from a dict
v1_transcodes_get200_response_from_dict = V1TranscodesGet200Response.from_dict(v1_transcodes_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


