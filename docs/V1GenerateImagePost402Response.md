# V1GenerateImagePost402Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**tokens_required** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**cancelled** | **bool** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_generate_image_post402_response import V1GenerateImagePost402Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1GenerateImagePost402Response from a JSON string
v1_generate_image_post402_response_instance = V1GenerateImagePost402Response.from_json(json)
# print the JSON string representation of the object
print(V1GenerateImagePost402Response.to_json())

# convert the object into a dict
v1_generate_image_post402_response_dict = v1_generate_image_post402_response_instance.to_dict()
# create an instance of V1GenerateImagePost402Response from a dict
v1_generate_image_post402_response_from_dict = V1GenerateImagePost402Response.from_dict(v1_generate_image_post402_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


