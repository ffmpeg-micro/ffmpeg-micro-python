# Transcribe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**TranscodeStatus**](TranscodeStatus.md) |  | 
**job_type** | **str** |  | [optional] 
**media_url** | **str** | GCS URL of the source audio/video (echoed from the request) | 
**input_url** | **str** | Same value as &#x60;media_url&#x60; (legacy field name on reads) | [optional] 
**output_format** | **str** | Always &#x60;srt&#x60; for transcribe jobs | 
**output_url** | **str** | &#x60;gs://&#x60; URL of the generated SRT once &#x60;status&#x60; is &#x60;completed&#x60;. Use &#x60;/v1/transcribe/{id}/download&#x60; to obtain a signed HTTPS URL.  | [optional] 
**error_message** | **str** | Populated when status is &#x60;failed&#x60; or &#x60;canceled&#x60; (\&quot;Job canceled by user\&quot;) | [optional] 
**error_category** | **str** | Machine classification derived from error_message (generated column). Only meaningful when status is &#x60;failed&#x60;; jobs with no error carry &#x60;unknown&#x60;, never null.  | [optional] 
**duration_seconds** | **float** | Duration of the source media (drives billing — input minutes) | [optional] 
**billable_minutes** | **float** | Billable minutes, metered per second on input duration (a 19-second job bills 0.3167). Not an integer.  | [optional] 
**processing_time_seconds** | **float** | Wall-clock processing time measured by the toolkit; null until completed | [optional] 
**queue_position** | **int** | Jobs waiting in the job&#39;s toolkit lane at acceptance, this one included: the accepting worker&#39;s queue length right after this job was enqueued, so 1 means it was next in line. Set once at acceptance and never updated: a rough \&quot;how far back was I\&quot;, not a live counter. Once &#x60;started_at&#x60; is set the job is no longer waiting, whatever this says. Null on jobs accepted before the field existed, or when the toolkit&#39;s accept response carried no queue length.  | [optional] 
**lane** | **str** | The processing lane the job runs in. Jobs with many large inputs (more than five 4K frames&#39; worth of pixels in total) go to &#x60;heavy&#x60;, a service with more memory. Otherwise, inputs longer than two minutes (by probed length or requested output span) go to &#x60;long&#x60;; everything else is &#x60;short&#x60;. Each lane is a separate service, so nothing in one can delay a job in another. Null on jobs accepted before lanes existed.  | [optional] 
**started_at** | **datetime** | When the toolkit began executing the job. Set as soon as encoding starts, so null means the job is still waiting in its lane and non-null with status &#x60;processing&#x60; means it is encoding now. If that start signal was missed, it is filled from the completion or failure report. &#x60;started_at - created_at&#x60; is submission-to-start and includes the gateway&#39;s own download and probe before dispatch, so it is an upper bound on queue wait, not the wait itself.  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**user_id** | **str** | Internal user identifier resolved from API key | [optional] 

## Example

```python
from ffmpeg_micro.models.transcribe import Transcribe

# TODO update the JSON string below
json = "{}"
# create an instance of Transcribe from a JSON string
transcribe_instance = Transcribe.from_json(json)
# print the JSON string representation of the object
print(Transcribe.to_json())

# convert the object into a dict
transcribe_dict = transcribe_instance.to_dict()
# create an instance of Transcribe from a dict
transcribe_from_dict = Transcribe.from_dict(transcribe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


