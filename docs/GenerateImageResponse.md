# GenerateImageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**aspect** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**tokens_charged** | **float** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.generate_image_response import GenerateImageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateImageResponse from a JSON string
generate_image_response_instance = GenerateImageResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateImageResponse.to_json())

# convert the object into a dict
generate_image_response_dict = generate_image_response_instance.to_dict()
# create an instance of GenerateImageResponse from a dict
generate_image_response_from_dict = GenerateImageResponse.from_dict(generate_image_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


