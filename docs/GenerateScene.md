# GenerateScene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Narration for this scene | [optional] 
**image_prompt** | **str** | English visual description for an image generator | [optional] 

## Example

```python
from ffmpeg_micro.models.generate_scene import GenerateScene

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateScene from a JSON string
generate_scene_instance = GenerateScene.from_json(json)
# print the JSON string representation of the object
print(GenerateScene.to_json())

# convert the object into a dict
generate_scene_dict = generate_scene_instance.to_dict()
# create an instance of GenerateScene from a dict
generate_scene_from_dict = GenerateScene.from_dict(generate_scene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


