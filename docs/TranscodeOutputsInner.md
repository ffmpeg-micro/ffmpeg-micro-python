# TranscodeOutputsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | gs:// URL of the output file | [optional] 
**filename** | **str** |  | [optional] 
**size_bytes** | **int** |  | [optional] 
**format** | **str** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.transcode_outputs_inner import TranscodeOutputsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodeOutputsInner from a JSON string
transcode_outputs_inner_instance = TranscodeOutputsInner.from_json(json)
# print the JSON string representation of the object
print(TranscodeOutputsInner.to_json())

# convert the object into a dict
transcode_outputs_inner_dict = transcode_outputs_inner_instance.to_dict()
# create an instance of TranscodeOutputsInner from a dict
transcode_outputs_inner_from_dict = TranscodeOutputsInner.from_dict(transcode_outputs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


