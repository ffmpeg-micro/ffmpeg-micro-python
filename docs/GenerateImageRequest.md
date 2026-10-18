# GenerateImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** |  | 
**aspect** | **str** |  | [optional] [default to 'landscape_16_9']
**model** | **str** | Ignored when &#x60;reference_urls&#x60; is given (references force &#x60;nano-banana&#x60;) | [optional] [default to 'flux-schnell']
**reference_urls** | **List[str]** | https images the result must stay faithful to (a character sheet, a product shot) | [optional] 
**seed** | **int** | Fixed seed for repeatability. Omit for random; &#x60;null&#x60; is rejected. | [optional] 

## Example

```python
from ffmpeg_micro.models.generate_image_request import GenerateImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateImageRequest from a JSON string
generate_image_request_instance = GenerateImageRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateImageRequest.to_json())

# convert the object into a dict
generate_image_request_dict = generate_image_request_instance.to_dict()
# create an instance of GenerateImageRequest from a dict
generate_image_request_from_dict = GenerateImageRequest.from_dict(generate_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


