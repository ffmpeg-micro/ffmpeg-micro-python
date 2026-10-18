# V1UploadConfirmPost200ResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_url** | **str** | GCS URL (&#x60;gs://…&#x60;) for use in transcode/transcribe requests | [optional] 
**download_url** | **str** | Short-lived (1 hour) signed HTTPS URL for the uploaded file | [optional] 
**filename** | **str** |  | [optional] 
**file_size** | **int** | Actual size in bytes as verified in GCS | [optional] 
**uploaded_at** | **datetime** |  | [optional] 
**metadata** | [**MediaMetadata**](MediaMetadata.md) | Best-effort media probe of the uploaded file. Empty object when the probe request itself fails. When the probe responds but cannot determine a value, sentinel values are returned rather than the key being omitted: &#x60;duration_seconds: 0&#x60;, &#x60;format: \&quot;unknown\&quot;&#x60;, &#x60;size_bytes: 0&#x60;. The other fields are present only when the probe reported them.  | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_upload_confirm_post200_response_result import V1UploadConfirmPost200ResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1UploadConfirmPost200ResponseResult from a JSON string
v1_upload_confirm_post200_response_result_instance = V1UploadConfirmPost200ResponseResult.from_json(json)
# print the JSON string representation of the object
print(V1UploadConfirmPost200ResponseResult.to_json())

# convert the object into a dict
v1_upload_confirm_post200_response_result_dict = v1_upload_confirm_post200_response_result_instance.to_dict()
# create an instance of V1UploadConfirmPost200ResponseResult from a dict
v1_upload_confirm_post200_response_result_from_dict = V1UploadConfirmPost200ResponseResult.from_dict(v1_upload_confirm_post200_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


