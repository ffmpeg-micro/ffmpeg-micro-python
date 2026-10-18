# TranscodeInputsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | GCS URL of the (possibly re-hosted) input | [optional] 
**filename** | **str** |  | [optional] 
**duration** | **float** | Seconds; 0 for still images | [optional] 
**format** | **str** |  | [optional] 
**size_bytes** | [**TranscodeInputsInnerSizeBytes**](TranscodeInputsInnerSizeBytes.md) |  | [optional] 
**download_url** | **str** | Short-lived signed HTTPS URL for the input | [optional] 
**options** | **List[object]** | Per-input FFmpeg options as submitted | [optional] 

## Example

```python
from ffmpeg_micro.models.transcode_inputs_inner import TranscodeInputsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodeInputsInner from a JSON string
transcode_inputs_inner_instance = TranscodeInputsInner.from_json(json)
# print the JSON string representation of the object
print(TranscodeInputsInner.to_json())

# convert the object into a dict
transcode_inputs_inner_dict = transcode_inputs_inner_instance.to_dict()
# create an instance of TranscodeInputsInner from a dict
transcode_inputs_inner_from_dict = TranscodeInputsInner.from_dict(transcode_inputs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


