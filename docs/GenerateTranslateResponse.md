# GenerateTranslateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**texts** | **List[str]** |  | [optional] 
**language** | **str** |  | [optional] 
**tokens_charged** | **float** |  | [optional] 

## Example

```python
from ffmpeg_micro.models.generate_translate_response import GenerateTranslateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateTranslateResponse from a JSON string
generate_translate_response_instance = GenerateTranslateResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateTranslateResponse.to_json())

# convert the object into a dict
generate_translate_response_dict = generate_translate_response_instance.to_dict()
# create an instance of GenerateTranslateResponse from a dict
generate_translate_response_from_dict = GenerateTranslateResponse.from_dict(generate_translate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


