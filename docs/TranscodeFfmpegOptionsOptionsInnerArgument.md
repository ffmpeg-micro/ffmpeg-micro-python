# TranscodeFfmpegOptionsOptionsInnerArgument

Flag value. Omitted (never null) for flag-only options (`-an`, `-vn`, `-shortest`) and whenever the caller sent null, so a bare flag serializes without one. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from ffmpeg_micro.models.transcode_ffmpeg_options_options_inner_argument import TranscodeFfmpegOptionsOptionsInnerArgument

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodeFfmpegOptionsOptionsInnerArgument from a JSON string
transcode_ffmpeg_options_options_inner_argument_instance = TranscodeFfmpegOptionsOptionsInnerArgument.from_json(json)
# print the JSON string representation of the object
print(TranscodeFfmpegOptionsOptionsInnerArgument.to_json())

# convert the object into a dict
transcode_ffmpeg_options_options_inner_argument_dict = transcode_ffmpeg_options_options_inner_argument_instance.to_dict()
# create an instance of TranscodeFfmpegOptionsOptionsInnerArgument from a dict
transcode_ffmpeg_options_options_inner_argument_from_dict = TranscodeFfmpegOptionsOptionsInnerArgument.from_dict(transcode_ffmpeg_options_options_inner_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


