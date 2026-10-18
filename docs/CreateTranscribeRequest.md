# CreateTranscribeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_url** | **str** | GCS URL (gs://bucket/object) from a presigned upload, or a public HTTP(S) URL. The referenced file can be audio or video — only the audio track is used.  | 
**language** | **str** | BCP-47 language code hint (e.g. \&quot;en\&quot;, \&quot;es\&quot;). Auto-detected when omitted. | [optional] 
**task** | **str** | \&quot;transcribe\&quot; keeps the source language; \&quot;translate\&quot; outputs English regardless of source language.  | [optional] [default to 'transcribe']

## Example

```python
from ffmpeg_micro.models.create_transcribe_request import CreateTranscribeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTranscribeRequest from a JSON string
create_transcribe_request_instance = CreateTranscribeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTranscribeRequest.to_json())

# convert the object into a dict
create_transcribe_request_dict = create_transcribe_request_instance.to_dict()
# create an instance of CreateTranscribeRequest from a dict
create_transcribe_request_from_dict = CreateTranscribeRequest.from_dict(create_transcribe_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


