# FFmpegOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | **str** | FFmpeg flag (e.g., -c:v, -crf, -preset) | 
**argument** | **str** | Flag value | 

## Example

```python
from ffmpeg_micro.models.f_fmpeg_option import FFmpegOption

# TODO update the JSON string below
json = "{}"
# create an instance of FFmpegOption from a JSON string
f_fmpeg_option_instance = FFmpegOption.from_json(json)
# print the JSON string representation of the object
print(FFmpegOption.to_json())

# convert the object into a dict
f_fmpeg_option_dict = f_fmpeg_option_instance.to_dict()
# create an instance of FFmpegOption from a dict
f_fmpeg_option_from_dict = FFmpegOption.from_dict(f_fmpeg_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


