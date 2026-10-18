# GenerateScenesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenes** | [**List[GenerateScene]**](GenerateScene.md) |  | [optional] 
**tokens_charged** | **float** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.generate_scenes_response import GenerateScenesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateScenesResponse from a JSON string
generate_scenes_response_instance = GenerateScenesResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateScenesResponse.to_json())

# convert the object into a dict
generate_scenes_response_dict = generate_scenes_response_instance.to_dict()
# create an instance of GenerateScenesResponse from a dict
generate_scenes_response_from_dict = GenerateScenesResponse.from_dict(generate_scenes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


