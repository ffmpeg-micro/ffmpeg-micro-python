# GenerateTranslateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**texts** | **List[str]** |  | 
**language** | **str** | ISO 639-1 target language, e.g. &#x60;fr&#x60; | 

## Example

```python
from ffmpeg_micro.models.generate_translate_request import GenerateTranslateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateTranslateRequest from a JSON string
generate_translate_request_instance = GenerateTranslateRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateTranslateRequest.to_json())

# convert the object into a dict
generate_translate_request_dict = generate_translate_request_instance.to_dict()
# create an instance of GenerateTranslateRequest from a dict
generate_translate_request_from_dict = GenerateTranslateRequest.from_dict(generate_translate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


