# V1GenerateScenesPost502Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 
**tokens_charged** | **float** |  | [optional] 
**refund** | **str** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_generate_scenes_post502_response import V1GenerateScenesPost502Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1GenerateScenesPost502Response from a JSON string
v1_generate_scenes_post502_response_instance = V1GenerateScenesPost502Response.from_json(json)
# print the JSON string representation of the object
print(V1GenerateScenesPost502Response.to_json())

# convert the object into a dict
v1_generate_scenes_post502_response_dict = v1_generate_scenes_post502_response_instance.to_dict()
# create an instance of V1GenerateScenesPost502Response from a dict
v1_generate_scenes_post502_response_from_dict = V1GenerateScenesPost502Response.from_dict(v1_generate_scenes_post502_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


