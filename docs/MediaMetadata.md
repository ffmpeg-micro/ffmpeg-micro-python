# MediaMetadata

What ffprobe reported about a media file. `duration_seconds`, `format` and `size_bytes` may carry `0` or `\"unknown\"` when the probe ran but could not determine them (a still image has no duration). `width`, `height`, `fps`, `codec_video`, `codec_audio`, `has_video` and `has_audio` are present only when the probe reported them: a plain audio file has no `width`. Cover art embedded in an audio file is a video stream to ffprobe, so such a file reports `has_video: true` with the artwork's dimensions. `width` and `height` are the stored dimensions, before any rotation the file carries: a phone video shot upright can report 1920 by 1080. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_seconds** | **float** |  | [optional] 
**format** | **str** | Container format as ffprobe names it | [optional] 
**size_bytes** | **int** |  | [optional] 
**width** | **int** | Video width in pixels; absent for audio-only files | [optional] 
**height** | **int** | Video height in pixels; absent for audio-only files | [optional] 
**fps** | **float** | Frame rate of the video stream; absent for audio-only files | [optional] 
**codec_video** | **str** | Codec of the video stream (e.g. h264); absent when there is none | [optional] 
**codec_audio** | **str** | Codec of the audio stream (e.g. aac); absent when there is none | [optional] 
**has_video** | **bool** | Whether the file has a video stream | [optional] 
**has_audio** | **bool** | Whether the file has an audio stream | [optional] 

## Example

```python
from ffmpeg_micro.models.media_metadata import MediaMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MediaMetadata from a JSON string
media_metadata_instance = MediaMetadata.from_json(json)
# print the JSON string representation of the object
print(MediaMetadata.to_json())

# convert the object into a dict
media_metadata_dict = media_metadata_instance.to_dict()
# create an instance of MediaMetadata from a dict
media_metadata_from_dict = MediaMetadata.from_dict(media_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


