# GenerateSpeechResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | mp3 | [optional] 
**characters** | **int** |  | [optional] 
**tokens_charged** | **float** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.generate_speech_response import GenerateSpeechResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSpeechResponse from a JSON string
generate_speech_response_instance = GenerateSpeechResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateSpeechResponse.to_json())

# convert the object into a dict
generate_speech_response_dict = generate_speech_response_instance.to_dict()
# create an instance of GenerateSpeechResponse from a dict
generate_speech_response_from_dict = GenerateSpeechResponse.from_dict(generate_speech_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


