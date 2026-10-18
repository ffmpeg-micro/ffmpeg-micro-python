# V1UploadPresignedUrlPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**result** | [**V1UploadPresignedUrlPost200ResponseResult**](V1UploadPresignedUrlPost200ResponseResult.md) |  | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_upload_presigned_url_post200_response import V1UploadPresignedUrlPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1UploadPresignedUrlPost200Response from a JSON string
v1_upload_presigned_url_post200_response_instance = V1UploadPresignedUrlPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1UploadPresignedUrlPost200Response.to_json())

# convert the object into a dict
v1_upload_presigned_url_post200_response_dict = v1_upload_presigned_url_post200_response_instance.to_dict()
# create an instance of V1UploadPresignedUrlPost200Response from a dict
v1_upload_presigned_url_post200_response_from_dict = V1UploadPresignedUrlPost200Response.from_dict(v1_upload_presigned_url_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


