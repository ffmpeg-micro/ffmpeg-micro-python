# V1UploadConfirmPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Filename returned from presigned URL generation | 
**file_size** | **int** | Actual uploaded size in bytes as a JSON number (must match the object in GCS). Same rules as presign: not a string, must be finite and positive.  | 
**upload_id** | **str** | Optional upload ID for tracking | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_upload_confirm_post_request import V1UploadConfirmPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1UploadConfirmPostRequest from a JSON string
v1_upload_confirm_post_request_instance = V1UploadConfirmPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1UploadConfirmPostRequest.to_json())

# convert the object into a dict
v1_upload_confirm_post_request_dict = v1_upload_confirm_post_request_instance.to_dict()
# create an instance of V1UploadConfirmPostRequest from a dict
v1_upload_confirm_post_request_from_dict = V1UploadConfirmPostRequest.from_dict(v1_upload_confirm_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


