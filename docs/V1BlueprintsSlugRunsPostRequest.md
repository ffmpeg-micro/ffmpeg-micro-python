# V1BlueprintsSlugRunsPostRequest

Per-slug inputs. product-ad: `logo_url`, `photo_url`, optional `music_url`. caption-video: `video_url`, optional `language`, `style`. viral-short: `video_url`, `hook_text`, optional `style`, `music_url`. quote-card: `quote`, optional `name`, `handle`, `photo_url` (profile photo; initials avatar without it). watermark: `video_url`, `logo_url`, optional `position` (top-left|top-right|bottom-left|bottom-right|center, default bottom-right), `size` (small|medium|large, default small). resize-format: `video_url`, optional `format` (9x16|1x1|16x9|4x5, default 9x16), `fit` (pad|crop, default pad). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo_url** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**video_url** | **str** |  | [optional] 
**hook_text** | **str** |  | [optional] 
**quote** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**handle** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**fit** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**music_url** | **str** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.v1_blueprints_slug_runs_post_request import V1BlueprintsSlugRunsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1BlueprintsSlugRunsPostRequest from a JSON string
v1_blueprints_slug_runs_post_request_instance = V1BlueprintsSlugRunsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V1BlueprintsSlugRunsPostRequest.to_json())

# convert the object into a dict
v1_blueprints_slug_runs_post_request_dict = v1_blueprints_slug_runs_post_request_instance.to_dict()
# create an instance of V1BlueprintsSlugRunsPostRequest from a dict
v1_blueprints_slug_runs_post_request_from_dict = V1BlueprintsSlugRunsPostRequest.from_dict(v1_blueprints_slug_runs_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


