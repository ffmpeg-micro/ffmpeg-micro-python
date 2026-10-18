# JobDetails

Detailed job information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**job_id** | **str** |  | 
**status** | [**TranscodeStatus**](TranscodeStatus.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**input_url** | **str** |  | [optional] 
**output_url** | **str** | GCS path to output file (gs://bucket/key) | [optional] 
**output_format** | **str** |  | [optional] 
**quality** | **str** |  | [optional] 
**resolution** | **str** |  | [optional] 
**processing_time_seconds** | **float** | Actual processing time in seconds | [optional] 
**duration_seconds** | **float** | Video duration in seconds | [optional] 
**metadata** | **object** | Additional job metadata | [optional] 
**error_message** | **str** | Error message if job failed | [optional] 
**completed_at** | **datetime** | When the job completed | [optional] 

## Example

```python
from ffmpeg_micro.models.job_details import JobDetails

# TODO update the JSON string below
json = "{}"
# create an instance of JobDetails from a JSON string
job_details_instance = JobDetails.from_json(json)
# print the JSON string representation of the object
print(JobDetails.to_json())

# convert the object into a dict
job_details_dict = job_details_instance.to_dict()
# create an instance of JobDetails from a dict
job_details_from_dict = JobDetails.from_dict(job_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


