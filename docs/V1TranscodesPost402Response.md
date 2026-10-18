# V1TranscodesPost402Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Human-readable refusal naming the remedy | 
**job_id** | **str** | The failed job row recording this blocked attempt | 
**upgrade_url** | **str** | Deep link to billing, carrying &#x60;job&#x3D;&lt;job_id&gt;&#x60; | 

## Example

```python
from ffmpeg_micro.models.v1_transcodes_post402_response import V1TranscodesPost402Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1TranscodesPost402Response from a JSON string
v1_transcodes_post402_response_instance = V1TranscodesPost402Response.from_json(json)
# print the JSON string representation of the object
print(V1TranscodesPost402Response.to_json())

# convert the object into a dict
v1_transcodes_post402_response_dict = v1_transcodes_post402_response_instance.to_dict()
# create an instance of V1TranscodesPost402Response from a dict
v1_transcodes_post402_response_from_dict = V1TranscodesPost402Response.from_dict(v1_transcodes_post402_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


