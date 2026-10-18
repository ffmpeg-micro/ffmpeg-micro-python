# GenerateScenesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** | The narration script, any language | 
**max_scenes** | **int** |  | [optional] [default to 6]

## Example

```python
from ffmpeg_micro.models.generate_scenes_request import GenerateScenesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateScenesRequest from a JSON string
generate_scenes_request_instance = GenerateScenesRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateScenesRequest.to_json())

# convert the object into a dict
generate_scenes_request_dict = generate_scenes_request_instance.to_dict()
# create an instance of GenerateScenesRequest from a dict
generate_scenes_request_from_dict = GenerateScenesRequest.from_dict(generate_scenes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


