# V1FfprobePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The &#x60;fileUrl&#x60; (a &#x60;gs://&#x60; address) returned by &#x60;POST /v1/upload/confirm&#x60;. | 

## Example

```python
from ffmpeg_micro.models.v1_ffprobe_post_request import V1FfprobePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1FfprobePostRequest from a JSON string
v1_ffprobe_post_request_instance = V1FfprobePostRequest.from_json(json)
# print the JSON string representation of the object
print(V1FfprobePostRequest.to_json())

# convert the object into a dict
v1_ffprobe_post_request_dict = v1_ffprobe_post_request_instance.to_dict()
# create an instance of V1FfprobePostRequest from a dict
v1_ffprobe_post_request_from_dict = V1FfprobePostRequest.from_dict(v1_ffprobe_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


