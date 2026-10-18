# VirtualOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | **str** | Virtual option name (prefixed with @) | 
**argument** | [**VirtualOptionArgument**](VirtualOptionArgument.md) |  | 

## Example

```python
from ffmpeg_micro.models.virtual_option import VirtualOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualOption from a JSON string
virtual_option_instance = VirtualOption.from_json(json)
# print the JSON string representation of the object
print(VirtualOption.to_json())

# convert the object into a dict
virtual_option_dict = virtual_option_instance.to_dict()
# create an instance of VirtualOption from a dict
virtual_option_from_dict = VirtualOption.from_dict(virtual_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


