# CreateTranscodeRequestPreset

Simple mode - quality and resolution presets (ignored if options provided)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quality** | **str** | Maps to CRF values (high&#x3D;18, medium&#x3D;23, low&#x3D;28) | [optional] 
**resolution** | **str** | Output resolution preset | [optional] 

## Example

```python
from ffmpeg_micro.models.create_transcode_request_preset import CreateTranscodeRequestPreset

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTranscodeRequestPreset from a JSON string
create_transcode_request_preset_instance = CreateTranscodeRequestPreset.from_json(json)
# print the JSON string representation of the object
print(CreateTranscodeRequestPreset.to_json())

# convert the object into a dict
create_transcode_request_preset_dict = create_transcode_request_preset_instance.to_dict()
# create an instance of CreateTranscodeRequestPreset from a dict
create_transcode_request_preset_from_dict = CreateTranscodeRequestPreset.from_dict(create_transcode_request_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


