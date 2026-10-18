# CreateTranscodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**List[CreateTranscodeRequestInputsInner]**](CreateTranscodeRequestInputsInner.md) | Array of input videos (single for transcode, multiple for composition) | 
**output_format** | **str** | Output container format — video (mp4, webm, mov, avi), audio (mp3, m4a, aac, wav, ogg, opus, flac) or image (jpeg/jpg, png, gif, webp). Validation is case/alias-insensitive (&#x60;jpg&#x60; &#x3D; &#x60;jpeg&#x60;), but the value is STORED VERBATIM and reads back exactly as submitted. webm output automatically uses VP9/Opus codecs in preset and default modes; you only need explicit &#x60;-c:v&#x60;/&#x60;-c:a&#x60; options when supplying raw options.  | 
**preset** | [**CreateTranscodeRequestPreset**](CreateTranscodeRequestPreset.md) |  | [optional] 
**options** | [**List[CreateTranscodeRequestOptionsInner]**](CreateTranscodeRequestOptionsInner.md) | Advanced mode - FFmpeg options or virtual options (overrides preset if both provided). **Virtual Options** (prefix with &#x60;@&#x60;): - &#x60;@text-overlay&#x60;: Add text overlay with auto word-wrap and styling **FFmpeg Options**: Only allowlisted flags accepted for security.  | [optional] 
**metadata** | **Dict[str, object]** | Optional caller-supplied metadata for cross-referencing jobs with external systems (for example an original filename or a source record ID). Must be a JSON object; serialized size is capped at 8192 bytes. Stored under the &#x60;user&#x60; key of the job&#39;s &#x60;metadata&#x60; field, so the submitted value is available at &#x60;metadata.user&#x60; when fetching or listing jobs, and is echoed as &#x60;metadata.user&#x60; in the create response.  | [optional] 

## Example

```python
from ffmpeg_micro.models.create_transcode_request import CreateTranscodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTranscodeRequest from a JSON string
create_transcode_request_instance = CreateTranscodeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTranscodeRequest.to_json())

# convert the object into a dict
create_transcode_request_dict = create_transcode_request_instance.to_dict()
# create an instance of CreateTranscodeRequest from a dict
create_transcode_request_from_dict = CreateTranscodeRequest.from_dict(create_transcode_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


