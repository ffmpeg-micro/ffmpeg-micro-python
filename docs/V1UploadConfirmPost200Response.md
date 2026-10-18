# V1UploadConfirmPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**result** | [**V1UploadConfirmPost200ResponseResult**](V1UploadConfirmPost200ResponseResult.md) |  | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_upload_confirm_post200_response import V1UploadConfirmPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1UploadConfirmPost200Response from a JSON string
v1_upload_confirm_post200_response_instance = V1UploadConfirmPost200Response.from_json(json)
# print the JSON string representation of the object
print(V1UploadConfirmPost200Response.to_json())

# convert the object into a dict
v1_upload_confirm_post200_response_dict = v1_upload_confirm_post200_response_instance.to_dict()
# create an instance of V1UploadConfirmPost200Response from a dict
v1_upload_confirm_post200_response_from_dict = V1UploadConfirmPost200Response.from_dict(v1_upload_confirm_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


