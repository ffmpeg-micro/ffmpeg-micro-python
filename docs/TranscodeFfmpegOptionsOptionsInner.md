# TranscodeFfmpegOptionsOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | **str** | FFmpeg flag (e.g. &#x60;-c:v&#x60;, &#x60;-crf&#x60;, &#x60;-f&#x60;) | 
**argument** | [**TranscodeFfmpegOptionsOptionsInnerArgument**](TranscodeFfmpegOptionsOptionsInnerArgument.md) |  | [optional] 

## Example

```python
from ffmpeg_micro.models.transcode_ffmpeg_options_options_inner import TranscodeFfmpegOptionsOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodeFfmpegOptionsOptionsInner from a JSON string
transcode_ffmpeg_options_options_inner_instance = TranscodeFfmpegOptionsOptionsInner.from_json(json)
# print the JSON string representation of the object
print(TranscodeFfmpegOptionsOptionsInner.to_json())

# convert the object into a dict
transcode_ffmpeg_options_options_inner_dict = transcode_ffmpeg_options_options_inner_instance.to_dict()
# create an instance of TranscodeFfmpegOptionsOptionsInner from a dict
transcode_ffmpeg_options_options_inner_from_dict = TranscodeFfmpegOptionsOptionsInner.from_dict(transcode_ffmpeg_options_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


