# GenerateAnimateQueued


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Poll handle for GET /v1/generate/animate/:id | [optional] 
**status** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**aspect** | **str** |  | [optional] 
**tokens_charged** | **float** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.generate_animate_queued import GenerateAnimateQueued

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAnimateQueued from a JSON string
generate_animate_queued_instance = GenerateAnimateQueued.from_json(json)
# print the JSON string representation of the object
print(GenerateAnimateQueued.to_json())

# convert the object into a dict
generate_animate_queued_dict = generate_animate_queued_instance.to_dict()
# create an instance of GenerateAnimateQueued from a dict
generate_animate_queued_from_dict = GenerateAnimateQueued.from_dict(generate_animate_queued_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


