# ProbeError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**details** | **List[str]** | The reason, in words written for the caller. | [optional] 

## Example

```python
from ffmpeg_micro.models.probe_error import ProbeError

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeError from a JSON string
probe_error_instance = ProbeError.from_json(json)
# print the JSON string representation of the object
print(ProbeError.to_json())

# convert the object into a dict
probe_error_dict = probe_error_instance.to_dict()
# create an instance of ProbeError from a dict
probe_error_from_dict = ProbeError.from_dict(probe_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


