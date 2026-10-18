# TranscodeInputsInnerSizeBytes

File size in bytes, as a decimal string the way the media probe reports it (`\"991017\"`; `\"0\"` when the probe gave no size). Older jobs may carry an integer. Parse it as a number before doing arithmetic. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ffmpeg_micro.models.transcode_inputs_inner_size_bytes import TranscodeInputsInnerSizeBytes

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodeInputsInnerSizeBytes from a JSON string
transcode_inputs_inner_size_bytes_instance = TranscodeInputsInnerSizeBytes.from_json(json)
# print the JSON string representation of the object
print(TranscodeInputsInnerSizeBytes.to_json())

# convert the object into a dict
transcode_inputs_inner_size_bytes_dict = transcode_inputs_inner_size_bytes_instance.to_dict()
# create an instance of TranscodeInputsInnerSizeBytes from a dict
transcode_inputs_inner_size_bytes_from_dict = TranscodeInputsInnerSizeBytes.from_dict(transcode_inputs_inner_size_bytes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


