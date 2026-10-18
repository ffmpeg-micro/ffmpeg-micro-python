# CreateTranscodeRequestOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | **str** | FFmpeg flag (e.g., -c:v, -crf, -preset) | 
**argument** | **str** | Flag value | 

## Example

```python
from ffmpeg_micro.models.create_transcode_request_options_inner import CreateTranscodeRequestOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTranscodeRequestOptionsInner from a JSON string
create_transcode_request_options_inner_instance = CreateTranscodeRequestOptionsInner.from_json(json)
# print the JSON string representation of the object
print(CreateTranscodeRequestOptionsInner.to_json())

# convert the object into a dict
create_transcode_request_options_inner_dict = create_transcode_request_options_inner_instance.to_dict()
# create an instance of CreateTranscodeRequestOptionsInner from a dict
create_transcode_request_options_inner_from_dict = CreateTranscodeRequestOptionsInner.from_dict(create_transcode_request_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


