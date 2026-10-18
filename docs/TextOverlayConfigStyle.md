# TextOverlayConfigStyle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chars_per_line** | **int** | Auto word-wrap at this character width (default: no wrap) | [optional] 
**font** | **str** | Font name (default: Arial) | [optional] 
**font_size** | **int** | Font size in pixels (default: 48) | [optional] 
**line_spacing** | **int** | Space between lines in pixels (default: 10) | [optional] 
**font_color** | **str** | Font color (default: white) | [optional] 
**x** | **str** | X position FFmpeg expression (default: (w-text_w)/2 for center) | [optional] 
**y** | **str** | Y position FFmpeg expression (default: (h-text_h)/2 for center) | [optional] 
**box_border_w** | **int** | Box padding/border width in pixels (default: 20) | [optional] 

## Example

```python
from ffmpeg_micro.models.text_overlay_config_style import TextOverlayConfigStyle

# TODO update the JSON string below
json = "{}"
# create an instance of TextOverlayConfigStyle from a JSON string
text_overlay_config_style_instance = TextOverlayConfigStyle.from_json(json)
# print the JSON string representation of the object
print(TextOverlayConfigStyle.to_json())

# convert the object into a dict
text_overlay_config_style_dict = text_overlay_config_style_instance.to_dict()
# create an instance of TextOverlayConfigStyle from a dict
text_overlay_config_style_from_dict = TextOverlayConfigStyle.from_dict(text_overlay_config_style_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


