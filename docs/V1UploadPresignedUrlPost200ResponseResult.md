# V1UploadPresignedUrlPost200ResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_url** | **str** | Presigned URL for HTTP PUT upload | [optional] 
**filename** | **str** | Final filename in GCS (with timestamp prefix) | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_upload_presigned_url_post200_response_result import V1UploadPresignedUrlPost200ResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1UploadPresignedUrlPost200ResponseResult from a JSON string
v1_upload_presigned_url_post200_response_result_instance = V1UploadPresignedUrlPost200ResponseResult.from_json(json)
# print the JSON string representation of the object
print(V1UploadPresignedUrlPost200ResponseResult.to_json())

# convert the object into a dict
v1_upload_presigned_url_post200_response_result_dict = v1_upload_presigned_url_post200_response_result_instance.to_dict()
# create an instance of V1UploadPresignedUrlPost200ResponseResult from a dict
v1_upload_presigned_url_post200_response_result_from_dict = V1UploadPresignedUrlPost200ResponseResult.from_dict(v1_upload_presigned_url_post200_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


