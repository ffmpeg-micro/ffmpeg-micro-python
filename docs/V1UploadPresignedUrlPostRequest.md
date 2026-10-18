# V1UploadPresignedUrlPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Original filename (will be prefixed with timestamp) | 
**content_type** | **str** | MIME type of the file. Must be one of the supported types below — note AVI is &#x60;video/x-msvideo&#x60; (not &#x60;video/avi&#x60;). Matroska/MKV is not supported.  | 
**file_size** | **int** | File size in bytes as a JSON number (not a string). Must be finite, positive, and under the hard cap of 1.9 GiB (2040109465 bytes). String values (including digit-only strings like \&quot;1024\&quot;) are rejected with 400. Plans also carry their own maximum input file size (100 MB on Free, 1 GB on Starter, 2 GB on Pro); that limit is checked asynchronously after job creation — an oversize input still returns 201 from POST /v1/transcodes and the job then transitions to &#x60;failed&#x60; with &#x60;error_category: file_size&#x60;.  | 

## Example

```python
from ffmpeg_micro.models.v1_upload_presigned_url_post_request import V1UploadPresignedUrlPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UploadPresignedUrlPostRequest from a JSON string
v1_upload_presigned_url_post_request_instance = V1UploadPresignedUrlPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1UploadPresignedUrlPostRequest.to_json())

# convert the object into a dict
v1_upload_presigned_url_post_request_dict = v1_upload_presigned_url_post_request_instance.to_dict()
# create an instance of V1UploadPresignedUrlPostRequest from a dict
v1_upload_presigned_url_post_request_from_dict = V1UploadPresignedUrlPostRequest.from_dict(v1_upload_presigned_url_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


