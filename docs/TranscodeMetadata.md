# TranscodeMetadata

Job metadata object. Caller-supplied metadata from the create request is echoed under `metadata.user` (JSON object, max 8 KB serialized). The object also carries internal keys written by the service (e.g. preset details, request origin, download token for the anonymous \"Try It\" flow) — treat keys other than `user` as opaque and unstable. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **object** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.transcode_metadata import TranscodeMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodeMetadata from a JSON string
transcode_metadata_instance = TranscodeMetadata.from_json(json)
# print the JSON string representation of the object
print(TranscodeMetadata.to_json())

# convert the object into a dict
transcode_metadata_dict = transcode_metadata_instance.to_dict()
# create an instance of TranscodeMetadata from a dict
transcode_metadata_from_dict = TranscodeMetadata.from_dict(transcode_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


