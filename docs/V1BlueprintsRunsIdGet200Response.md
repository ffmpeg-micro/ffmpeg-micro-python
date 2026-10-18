# V1BlueprintsRunsIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**blueprint** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**step** | **str** |  | [optional] 
**output_url** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**tokens_spent** | **int** |  | [optional] 
**srt_text** | **str** | Present only while an Auto Captions run awaits transcript review | [optional] 
**created_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_blueprints_runs_id_get200_response import V1BlueprintsRunsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V1BlueprintsRunsIdGet200Response from a JSON string
v1_blueprints_runs_id_get200_response_instance = V1BlueprintsRunsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(V1BlueprintsRunsIdGet200Response.to_json())

# convert the object into a dict
v1_blueprints_runs_id_get200_response_dict = v1_blueprints_runs_id_get200_response_instance.to_dict()
# create an instance of V1BlueprintsRunsIdGet200Response from a dict
v1_blueprints_runs_id_get200_response_from_dict = V1BlueprintsRunsIdGet200Response.from_dict(v1_blueprints_runs_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


