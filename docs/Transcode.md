# Transcode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**TranscodeStatus**](TranscodeStatus.md) |  | 
**inputs** | [**List[TranscodeInputsInner]**](TranscodeInputsInner.md) | Array of processed input metadata, populated at enqueue from the media probe.  | [optional] 
**outputs** | [**List[TranscodeOutputsInner]**](TranscodeOutputsInner.md) | Output file records, populated on completion | [optional] 
**output_format** | **str** | Output format as submitted — the value is stored verbatim, so a job created with &#x60;jpg&#x60; or &#x60;MP4&#x60; reads back exactly that way (validation is case/alias-insensitive; canonical values are mp4, webm, mov, avi, mp3, m4a, aac, wav, ogg, opus, flac, jpeg, png, gif, webp). Rows with &#x60;job_type: transcribe&#x60; carry &#x60;srt&#x60;.  | 
**job_type** | **str** | Discriminator — transcode and transcribe jobs share this resource shape and both appear in &#x60;GET /v1/transcodes&#x60; listings (there is no job_type filter). Transcribe rows additionally carry &#x60;media_url&#x60;.  | [optional] 
**billable_minutes** | **float** | Billable minutes, metered per second on input duration (a 19-second job bills 0.3167). Not an integer.  | [optional] 
**duration_seconds** | **float** | While the job is pending/processing: the billable input span (sum of input durations after trim options such as &#x60;-ss&#x60;/&#x60;-t&#x60;). Once completed: replaced by the measured duration of the OUTPUT file, which can differ from the input span (e.g. loops run longer). Billing always uses the input-side value.  | [optional] 
**processing_time_seconds** | **float** | Wall-clock processing time measured by the toolkit; null until completed | [optional] 
**queue_position** | **int** | Jobs waiting in the job&#39;s toolkit lane at acceptance, this one included: the accepting worker&#39;s queue length right after this job was enqueued, so 1 means it was next in line. Set once at acceptance and never updated: a rough \&quot;how far back was I\&quot;, not a live counter. Once &#x60;started_at&#x60; is set the job is no longer waiting, whatever this says. Null on jobs accepted before the field existed, or when the toolkit&#39;s accept response carried no queue length.  | [optional] 
**lane** | **str** | The processing lane the job runs in. Jobs with many large inputs (more than five 4K frames&#39; worth of pixels in total) go to &#x60;heavy&#x60;, a service with more memory. Otherwise, inputs longer than two minutes (by probed length or requested output span) go to &#x60;long&#x60;; everything else is &#x60;short&#x60;. Each lane is a separate service, so nothing in one can delay a job in another. Null on jobs accepted before lanes existed.  | [optional] 
**started_at** | **datetime** | When the toolkit began executing the job. Set as soon as encoding starts, so null means the job is still waiting in its lane and non-null with status &#x60;processing&#x60; means it is encoding now. If that start signal was missed, it is filled from the completion or failure report. &#x60;started_at - created_at&#x60; is submission-to-start and includes the gateway&#39;s own download and probe before dispatch, so it is an upper bound on queue wait, not the wait itself.  | [optional] 
**error_message** | **str** | Populated when status is &#x60;failed&#x60;, and also on user cancellation (&#x60;canceled&#x60; jobs carry \&quot;Job canceled by user\&quot;) — do not treat non-null error_message alone as job failure.  | [optional] 
**error_category** | **str** | Machine classification derived from error_message (generated column). Only meaningful when status is &#x60;failed&#x60;; jobs with no error carry &#x60;unknown&#x60;, never null. &#x60;processing_limit&#x60; is reserved for a job stopped at a per-job processing ceiling; no deployed release emits it yet (the ceiling ships separately).  | [optional] 
**completed_at** | **datetime** | Set on successful completion only — failed jobs keep this null | [optional] 
**metadata** | [**TranscodeMetadata**](TranscodeMetadata.md) |  | [optional] 
**ffmpeg_options** | [**TranscodeFfmpegOptions**](TranscodeFfmpegOptions.md) |  | [optional] 
**output_url** | **str** | Populated when status &#x3D; completed | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**user_id** | **str** | Internal user identifier resolved from API key | [optional] 
**input_url** | **str** | [DEPRECATED] Use inputs array instead | [optional] 

## Example

```python
from ffmpeg_micro.models.transcode import Transcode

# TODO update the JSON string below
json = "{}"
# create an instance of Transcode from a JSON string
transcode_instance = Transcode.from_json(json)
# print the JSON string representation of the object
print(Transcode.to_json())

# convert the object into a dict
transcode_dict = transcode_instance.to_dict()
# create an instance of Transcode from a dict
transcode_from_dict = Transcode.from_dict(transcode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


