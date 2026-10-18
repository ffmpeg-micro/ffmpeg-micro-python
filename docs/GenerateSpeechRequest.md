# GenerateSpeechRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**voice** | **str** | Provider voice name; omit for the default narrator | [optional] 

## Example

```python
from ffmpeg_micro.models.generate_speech_request import GenerateSpeechRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSpeechRequest from a JSON string
generate_speech_request_instance = GenerateSpeechRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateSpeechRequest.to_json())

# convert the object into a dict
generate_speech_request_dict = generate_speech_request_instance.to_dict()
# create an instance of GenerateSpeechRequest from a dict
generate_speech_request_from_dict = GenerateSpeechRequest.from_dict(generate_speech_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


