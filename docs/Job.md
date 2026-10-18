# Job

Summary job information for list views

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | [**TranscodeStatus**](TranscodeStatus.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**output_url** | **str** | GCS path to output file (gs://bucket/key) | [optional] 

## Example

```python
from ffmpeg_micro.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


