# TranscodeFfmpegOptions

Final FFmpeg options used (audit trail)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | How the options were derived. &#x60;raw_options&#x60;: the caller&#39;s &#x60;options&#x60;, sanitized. &#x60;virtual_options&#x60;: the caller&#39;s &#x60;options&#x60; included a virtual option (for example &#x60;@text-overlay&#x60;) that the gateway expanded. &#x60;preset&#x60;: a named preset. &#x60;defaults&#x60;: neither options nor a preset was given.  | [optional] 
**options** | [**List[TranscodeFfmpegOptionsOptionsInner]**](TranscodeFfmpegOptionsOptionsInner.md) | The normalized option list handed to FFmpeg, in order. | [optional] 
**preset** | **object** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.transcode_ffmpeg_options import TranscodeFfmpegOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TranscodeFfmpegOptions from a JSON string
transcode_ffmpeg_options_instance = TranscodeFfmpegOptions.from_json(json)
# print the JSON string representation of the object
print(TranscodeFfmpegOptions.to_json())

# convert the object into a dict
transcode_ffmpeg_options_dict = transcode_ffmpeg_options_instance.to_dict()
# create an instance of TranscodeFfmpegOptions from a dict
transcode_ffmpeg_options_from_dict = TranscodeFfmpegOptions.from_dict(transcode_ffmpeg_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


