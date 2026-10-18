# GenerateAnimateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | https start frame | 
**prompt** | **str** | What moves and how | 
**duration** | **int** |  | [optional] [default to 5]
**aspect** | **str** |  | [optional] [default to '16:9']
**negative_prompt** | **str** | What the motion must not introduce | [optional] 

## Example

```python
from ffmpeg_micro.models.generate_animate_request import GenerateAnimateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAnimateRequest from a JSON string
generate_animate_request_instance = GenerateAnimateRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateAnimateRequest.to_json())

# convert the object into a dict
generate_animate_request_dict = generate_animate_request_instance.to_dict()
# create an instance of GenerateAnimateRequest from a dict
generate_animate_request_from_dict = GenerateAnimateRequest.from_dict(generate_animate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


