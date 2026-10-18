# TranscribeCreated

Acknowledgement returned by `POST /v1/transcribe` — a subset of the full Transcribe resource. Poll `GET /v1/transcribe/{id}` for the full shape. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** | New transcribe jobs always start as &#x60;pending&#x60; | 
**media_url** | **str** | GCS URL of the source audio/video (echoed from the request) | 
**output_format** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from ffmpeg_micro.models.transcribe_created import TranscribeCreated

# TODO update the JSON string below
json = "{}"
# create an instance of TranscribeCreated from a JSON string
transcribe_created_instance = TranscribeCreated.from_json(json)
# print the JSON string representation of the object
print(TranscribeCreated.to_json())

# convert the object into a dict
transcribe_created_dict = transcribe_created_instance.to_dict()
# create an instance of TranscribeCreated from a dict
transcribe_created_from_dict = TranscribeCreated.from_dict(transcribe_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


