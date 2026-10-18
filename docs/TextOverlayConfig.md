# TextOverlayConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text to display (use \\n for manual line breaks, or use charsPerLine for auto word-wrap) | 
**style** | [**TextOverlayConfigStyle**](TextOverlayConfigStyle.md) |  | [optional] 

## Example

```python
from ffmpeg_micro.models.text_overlay_config import TextOverlayConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TextOverlayConfig from a JSON string
text_overlay_config_instance = TextOverlayConfig.from_json(json)
# print the JSON string representation of the object
print(TextOverlayConfig.to_json())

# convert the object into a dict
text_overlay_config_dict = text_overlay_config_instance.to_dict()
# create an instance of TextOverlayConfig from a dict
text_overlay_config_from_dict = TextOverlayConfig.from_dict(text_overlay_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


