# GenerateAnimateStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**url** | **str** | Present when &#x60;completed&#x60; (signed | [optional] 
**detail** | **str** | Present when &#x60;failed&#x60; | [optional] 
**retry_after_seconds** | **int** | Present when &#x60;unknown&#x60; | [optional] 
**tokens_charged** | **float** | 0 after a refund; unchanged while queued/processing/unknown | [optional] 
**refund** | **str** | Present only if a refund could not be recorded | [optional] 

## Example

```python
from ffmpeg_micro.models.generate_animate_status import GenerateAnimateStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAnimateStatus from a JSON string
generate_animate_status_instance = GenerateAnimateStatus.from_json(json)
# print the JSON string representation of the object
print(GenerateAnimateStatus.to_json())

# convert the object into a dict
generate_animate_status_dict = generate_animate_status_instance.to_dict()
# create an instance of GenerateAnimateStatus from a dict
generate_animate_status_from_dict = GenerateAnimateStatus.from_dict(generate_animate_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


