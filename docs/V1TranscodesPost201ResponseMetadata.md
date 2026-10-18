# V1TranscodesPost201ResponseMetadata

Present only when the request carried `metadata`; echoed as `metadata.user`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **object** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_transcodes_post201_response_metadata import V1TranscodesPost201ResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of V1TranscodesPost201ResponseMetadata from a JSON string
v1_transcodes_post201_response_metadata_instance = V1TranscodesPost201ResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(V1TranscodesPost201ResponseMetadata.to_json())

# convert the object into a dict
v1_transcodes_post201_response_metadata_dict = v1_transcodes_post201_response_metadata_instance.to_dict()
# create an instance of V1TranscodesPost201ResponseMetadata from a dict
v1_transcodes_post201_response_metadata_from_dict = V1TranscodesPost201ResponseMetadata.from_dict(v1_transcodes_post201_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


