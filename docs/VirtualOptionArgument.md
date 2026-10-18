# VirtualOptionArgument

Configuration object for the virtual option

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text to display (use \\n for manual line breaks, or use charsPerLine for auto word-wrap) | 
**style** | [**TextOverlayConfigStyle**](TextOverlayConfigStyle.md) |  | [optional] 

## Example

```python
from ffmpeg_micro.models.virtual_option_argument import VirtualOptionArgument

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualOptionArgument from a JSON string
virtual_option_argument_instance = VirtualOptionArgument.from_json(json)
# print the JSON string representation of the object
print(VirtualOptionArgument.to_json())

# convert the object into a dict
virtual_option_argument_dict = virtual_option_argument_instance.to_dict()
# create an instance of VirtualOptionArgument from a dict
virtual_option_argument_from_dict = VirtualOptionArgument.from_dict(virtual_option_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


