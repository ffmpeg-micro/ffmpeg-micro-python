# V1TranscribesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Transcribe]**](Transcribe.md) |  | [optional] 
**page** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_transcribes_get200_response import V1TranscribesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1TranscribesGet200Response from a JSON string
v1_transcribes_get200_response_instance = V1TranscribesGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1TranscribesGet200Response.to_json())

# convert the object into a dict
v1_transcribes_get200_response_dict = v1_transcribes_get200_response_instance.to_dict()
# create an instance of V1TranscribesGet200Response from a dict
v1_transcribes_get200_response_from_dict = V1TranscribesGet200Response.from_dict(v1_transcribes_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


