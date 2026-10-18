# CreateTranscodeRequestInputsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | GCS URL (gs://bucket/object) from presigned upload, or public HTTP(S) URL. Prefer gs:// to avoid egress charges.  | 

## Example

```python
from ffmpeg_micro.models.create_transcode_request_inputs_inner import CreateTranscodeRequestInputsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTranscodeRequestInputsInner from a JSON string
create_transcode_request_inputs_inner_instance = CreateTranscodeRequestInputsInner.from_json(json)
# print the JSON string representation of the object
print(CreateTranscodeRequestInputsInner.to_json())

# convert the object into a dict
create_transcode_request_inputs_inner_dict = create_transcode_request_inputs_inner_instance.to_dict()
# create an instance of CreateTranscodeRequestInputsInner from a dict
create_transcode_request_inputs_inner_from_dict = CreateTranscodeRequestInputsInner.from_dict(create_transcode_request_inputs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


