# ffmpeg_micro.DefaultApi

All URIs are relative to *https://api.ffmpeg-micro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_blueprints_runs_id_continue_post**](DefaultApi.md#v1_blueprints_runs_id_continue_post) | **POST** /v1/blueprints/runs/{id}/continue | Resume a paused run with a reviewed transcript
[**v1_blueprints_runs_id_get**](DefaultApi.md#v1_blueprints_runs_id_get) | **GET** /v1/blueprints/runs/{id} | Poll a blueprint run
[**v1_blueprints_slug_runs_post**](DefaultApi.md#v1_blueprints_slug_runs_post) | **POST** /v1/blueprints/{slug}/runs | Start a blueprint run (server-side recipe pipeline)
[**v1_ffprobe_post**](DefaultApi.md#v1_ffprobe_post) | **POST** /v1/ffprobe | Read an uploaded file&#39;s details (free)
[**v1_generate_animate_id_get**](DefaultApi.md#v1_generate_animate_id_get) | **GET** /v1/generate/animate/{id} | Poll an animation
[**v1_generate_animate_post**](DefaultApi.md#v1_generate_animate_post) | **POST** /v1/generate/animate | Animate an image into a video clip (18 tokens per second)
[**v1_generate_image_post**](DefaultApi.md#v1_generate_image_post) | **POST** /v1/generate/image | Generate an image (6 or 10 tokens)
[**v1_generate_scenes_post**](DefaultApi.md#v1_generate_scenes_post) | **POST** /v1/generate/scenes | Split a narration script into scenes (free)
[**v1_generate_speech_post**](DefaultApi.md#v1_generate_speech_post) | **POST** /v1/generate/speech | Generate speech from text (25 tokens per 1,000 characters)
[**v1_generate_translate_post**](DefaultApi.md#v1_generate_translate_post) | **POST** /v1/generate/translate | Translate an ordered list of narrations (free)
[**v1_transcodes_get**](DefaultApi.md#v1_transcodes_get) | **GET** /v1/transcodes | List transcodes (for the authenticated user)
[**v1_transcodes_id_cancel_patch**](DefaultApi.md#v1_transcodes_id_cancel_patch) | **PATCH** /v1/transcodes/{id}/cancel | Cancel a transcode job
[**v1_transcodes_id_download_get**](DefaultApi.md#v1_transcodes_id_download_get) | **GET** /v1/transcodes/{id}/download | Get a signed download URL for a completed transcode
[**v1_transcodes_id_get**](DefaultApi.md#v1_transcodes_id_get) | **GET** /v1/transcodes/{id} | Get a transcode
[**v1_transcodes_post**](DefaultApi.md#v1_transcodes_post) | **POST** /v1/transcodes | Create a transcode or multi-video composition
[**v1_transcribe_id_download_get**](DefaultApi.md#v1_transcribe_id_download_get) | **GET** /v1/transcribe/{id}/download | Get a signed download URL for the generated SRT
[**v1_transcribe_id_get**](DefaultApi.md#v1_transcribe_id_get) | **GET** /v1/transcribe/{id} | Get transcribe job status
[**v1_transcribe_post**](DefaultApi.md#v1_transcribe_post) | **POST** /v1/transcribe | Create a transcribe job (audio → SRT)
[**v1_transcribes_get**](DefaultApi.md#v1_transcribes_get) | **GET** /v1/transcribes | List transcribe jobs (for the authenticated user)
[**v1_upload_confirm_post**](DefaultApi.md#v1_upload_confirm_post) | **POST** /v1/upload/confirm | Confirm file upload
[**v1_upload_presigned_url_post**](DefaultApi.md#v1_upload_presigned_url_post) | **POST** /v1/upload/presigned-url | Generate presigned upload URL


# **v1_blueprints_runs_id_continue_post**
> V1BlueprintsRunsIdContinuePost200Response v1_blueprints_runs_id_continue_post(id, v1_blueprints_runs_id_continue_post_request)

Resume a paused run with a reviewed transcript

For `caption-video` runs in `awaiting_review`: submit the (possibly edited) SRT and the burn continues in the background. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.v1_blueprints_runs_id_continue_post200_response import V1BlueprintsRunsIdContinuePost200Response
from ffmpeg_micro.models.v1_blueprints_runs_id_continue_post_request import V1BlueprintsRunsIdContinuePostRequest
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    id = 'id_example' # str | 
    v1_blueprints_runs_id_continue_post_request = ffmpeg_micro.V1BlueprintsRunsIdContinuePostRequest() # V1BlueprintsRunsIdContinuePostRequest | 

    try:
        # Resume a paused run with a reviewed transcript
        api_response = api_instance.v1_blueprints_runs_id_continue_post(id, v1_blueprints_runs_id_continue_post_request)
        print("The response of DefaultApi->v1_blueprints_runs_id_continue_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_blueprints_runs_id_continue_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **v1_blueprints_runs_id_continue_post_request** | [**V1BlueprintsRunsIdContinuePostRequest**](V1BlueprintsRunsIdContinuePostRequest.md)|  | 

### Return type

[**V1BlueprintsRunsIdContinuePost200Response**](V1BlueprintsRunsIdContinuePost200Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Burn resumed |  -  |
**400** | Missing or oversized srt_text |  -  |
**401** | Missing/invalid API key |  -  |
**404** | Run not found |  -  |
**409** | Run is not awaiting review |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_blueprints_runs_id_get**
> V1BlueprintsRunsIdGet200Response v1_blueprints_runs_id_get(id)

Poll a blueprint run

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.v1_blueprints_runs_id_get200_response import V1BlueprintsRunsIdGet200Response
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Poll a blueprint run
        api_response = api_instance.v1_blueprints_runs_id_get(id)
        print("The response of DefaultApi->v1_blueprints_runs_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_blueprints_runs_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1BlueprintsRunsIdGet200Response**](V1BlueprintsRunsIdGet200Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run status and, when completed, a signed output URL (10 min TTL) |  -  |
**401** | Missing/invalid API key |  -  |
**404** | Run not found (or belongs to another user) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_blueprints_slug_runs_post**
> V1BlueprintsSlugRunsPost201Response v1_blueprints_slug_runs_post(slug, v1_blueprints_slug_runs_post_request)

Start a blueprint run (server-side recipe pipeline)

Kick off a blueprint recipe as a background pipeline. Available slugs: `product-ad` (generative; charges tokens server-side, 402 when the balance is insufficient), `caption-video` (transcribe then burn; pauses at `awaiting_review` for transcript edits), `viral-short` (optional audio swap then hook overlay), `quote-card` (styled quote card on the dark background; no media input required), `watermark` (logo overlay at a chosen corner and size), `resize-format` (reframe to a target aspect by pad or crop). Inputs are URLs from the upload chain (`gs://` in the upload bucket) or public HTTPS URLs. Poll `GET /v1/blueprints/runs/{id}` for progress; runs continue in the background after the client disconnects. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.v1_blueprints_slug_runs_post201_response import V1BlueprintsSlugRunsPost201Response
from ffmpeg_micro.models.v1_blueprints_slug_runs_post_request import V1BlueprintsSlugRunsPostRequest
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    slug = 'slug_example' # str | 
    v1_blueprints_slug_runs_post_request = ffmpeg_micro.V1BlueprintsSlugRunsPostRequest() # V1BlueprintsSlugRunsPostRequest | 

    try:
        # Start a blueprint run (server-side recipe pipeline)
        api_response = api_instance.v1_blueprints_slug_runs_post(slug, v1_blueprints_slug_runs_post_request)
        print("The response of DefaultApi->v1_blueprints_slug_runs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_blueprints_slug_runs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **v1_blueprints_slug_runs_post_request** | [**V1BlueprintsSlugRunsPostRequest**](V1BlueprintsSlugRunsPostRequest.md)|  | 

### Return type

[**V1BlueprintsSlugRunsPost201Response**](V1BlueprintsSlugRunsPost201Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Run created (pipeline executing in the background) |  -  |
**400** | Invalid or missing inputs |  -  |
**401** | Missing/invalid API key |  -  |
**402** | Insufficient token balance (generative blueprints) |  -  |
**404** | Unknown blueprint slug |  -  |
**429** | Too many active generative runs for this account |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ffprobe_post**
> V1FfprobePost200Response v1_ffprobe_post(v1_ffprobe_post_request)

Read an uploaded file's details (free)

Run ffprobe on a file you have uploaded and get back what it reports: duration, container format, size, dimensions, frame rate, codecs, and whether it has video and audio. No job is created and no tokens are charged. The file is named by the `gs://` address that `POST /v1/upload/confirm` returned; that response already carries the same details for a file you just uploaded. A public HTTP(S) address is not accepted: upload the file first. Your plan's per-file size limit applies. Rate limited to 30 requests per minute per API key. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.v1_ffprobe_post200_response import V1FfprobePost200Response
from ffmpeg_micro.models.v1_ffprobe_post_request import V1FfprobePostRequest
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    v1_ffprobe_post_request = ffmpeg_micro.V1FfprobePostRequest() # V1FfprobePostRequest | 

    try:
        # Read an uploaded file's details (free)
        api_response = api_instance.v1_ffprobe_post(v1_ffprobe_post_request)
        print("The response of DefaultApi->v1_ffprobe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_ffprobe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_ffprobe_post_request** | [**V1FfprobePostRequest**](V1FfprobePostRequest.md)|  | 

### Return type

[**V1FfprobePost200Response**](V1FfprobePost200Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | What ffprobe reported |  -  |
**400** | The &#x60;url&#x60; is missing or not acceptable. &#x60;error&#x60; is one of &#x60;Missing required field: url&#x60;, &#x60;Unsupported URL&#x60; (anything that is not a &#x60;gs://&#x60; address), &#x60;Placeholder bucket name&#x60;, &#x60;Invalid input&#x60; or &#x60;Invalid GCS URL&#x60;.  |  -  |
**401** | Missing/invalid API key |  -  |
**404** | No uploaded file has that address. |  -  |
**422** | &#x60;File too large&#x60;: the file is over your plan&#39;s per-file limit. &#x60;Could not read media&#x60;: ffprobe could not read it as audio, video or an image.  |  -  |
**429** | More than 30 requests in a minute from this API key. |  -  |
**502** | The probe could not run right now. Nothing was charged; try again. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_generate_animate_id_get**
> GenerateAnimateStatus v1_generate_animate_id_get(id)

Poll an animation

Status of a render you submitted. `queued` / `processing` mean keep polling; `completed` carries the video `url` (a signed URL — download promptly); `failed` means the tokens were refunded. A 503 with `status: unknown` means the provider could not be reached for the moment — the render is untouched and still charged; retry after `retry_after_seconds`. Only your own renders are visible. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.generate_animate_status import GenerateAnimateStatus
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    id = 'id_example' # str | The `id` returned by `POST /v1/generate/animate`

    try:
        # Poll an animation
        api_response = api_instance.v1_generate_animate_id_get(id)
        print("The response of DefaultApi->v1_generate_animate_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_generate_animate_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The &#x60;id&#x60; returned by &#x60;POST /v1/generate/animate&#x60; | 

### Return type

[**GenerateAnimateStatus**](GenerateAnimateStatus.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Render state |  -  |
**401** | Missing/invalid API key |  -  |
**404** | No render with that id belongs to the caller |  -  |
**503** | Provider unreachable; the render is unaffected. Retry after &#x60;retry_after_seconds&#x60;. |  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_generate_animate_post**
> GenerateAnimateQueued v1_generate_animate_post(generate_animate_request)

Animate an image into a video clip (18 tokens per second)

Image to video (Kling 2.5 Turbo Pro), 5 or 10 seconds. Asynchronous: the balance is checked, the render is submitted, and the tokens are charged under the returned `id`. Poll `GET /v1/generate/animate/{id}` until `completed` or `failed`; a failed render is refunded on that poll. If the render cannot be charged after submit it is cancelled and the response carries its `id` and `cancelled`. Rate limited to 30/min. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.generate_animate_queued import GenerateAnimateQueued
from ffmpeg_micro.models.generate_animate_request import GenerateAnimateRequest
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    generate_animate_request = ffmpeg_micro.GenerateAnimateRequest() # GenerateAnimateRequest | 

    try:
        # Animate an image into a video clip (18 tokens per second)
        api_response = api_instance.v1_generate_animate_post(generate_animate_request)
        print("The response of DefaultApi->v1_generate_animate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_generate_animate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_animate_request** | [**GenerateAnimateRequest**](GenerateAnimateRequest.md)|  | 

### Return type

[**GenerateAnimateQueued**](GenerateAnimateQueued.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Render queued and charged |  -  |
**400** | Invalid input (charged nothing) |  -  |
**401** | Missing/invalid API key |  -  |
**402** | Not enough tokens for this call; nothing was charged (for &#x60;animate&#x60;, &#x60;id&#x60; and &#x60;cancelled&#x60; are present if a render had already been submitted) |  -  |
**429** | Per-API-key rate limit exceeded (free routes 60/min, paid routes 30/min); see &#x60;x-ratelimit-*&#x60; headers |  -  |
**502** | The provider failed; any tokens spent were refunded unless &#x60;refund&#x60; says otherwise |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_generate_image_post**
> GenerateImageResponse v1_generate_image_post(generate_image_request)

Generate an image (6 or 10 tokens)

Text to image. Default model `flux-schnell` bills 6 tokens per image. `model: nano-banana` (10 tokens) follows style instructions more faithfully. With `reference_urls` (1–4 https images) the result is an EDIT that keeps the referenced character and product identical — the way to build a consistent storyboard; references force `nano-banana`. Tokens are spent before the provider call and refunded if it fails. Rate limited to 30/min per key. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.generate_image_request import GenerateImageRequest
from ffmpeg_micro.models.generate_image_response import GenerateImageResponse
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    generate_image_request = ffmpeg_micro.GenerateImageRequest() # GenerateImageRequest | 

    try:
        # Generate an image (6 or 10 tokens)
        api_response = api_instance.v1_generate_image_post(generate_image_request)
        print("The response of DefaultApi->v1_generate_image_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_generate_image_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_image_request** | [**GenerateImageRequest**](GenerateImageRequest.md)|  | 

### Return type

[**GenerateImageResponse**](GenerateImageResponse.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image generated |  -  |
**400** | Invalid input (charged nothing) |  -  |
**401** | Missing/invalid API key |  -  |
**402** | Not enough tokens for this call; nothing was charged (for &#x60;animate&#x60;, &#x60;id&#x60; and &#x60;cancelled&#x60; are present if a render had already been submitted) |  -  |
**429** | Per-API-key rate limit exceeded (free routes 60/min, paid routes 30/min); see &#x60;x-ratelimit-*&#x60; headers |  -  |
**502** | The provider failed; any tokens spent were refunded unless &#x60;refund&#x60; says otherwise |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_generate_scenes_post**
> GenerateScenesResponse v1_generate_scenes_post(generate_scenes_request)

Split a narration script into scenes (free)

Break a script into ordered scenes, each with the narration for that scene (same language as the input) and an English image prompt for it. Free: it is the step you iterate on before committing to paid images and speech. Rate limited to 60 requests per minute per API key. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.generate_scenes_request import GenerateScenesRequest
from ffmpeg_micro.models.generate_scenes_response import GenerateScenesResponse
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    generate_scenes_request = ffmpeg_micro.GenerateScenesRequest() # GenerateScenesRequest | 

    try:
        # Split a narration script into scenes (free)
        api_response = api_instance.v1_generate_scenes_post(generate_scenes_request)
        print("The response of DefaultApi->v1_generate_scenes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_generate_scenes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_scenes_request** | [**GenerateScenesRequest**](GenerateScenesRequest.md)|  | 

### Return type

[**GenerateScenesResponse**](GenerateScenesResponse.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scenes |  -  |
**400** | Invalid input |  -  |
**401** | Missing/invalid API key |  -  |
**429** | Per-API-key rate limit exceeded (free routes 60/min, paid routes 30/min); see &#x60;x-ratelimit-*&#x60; headers |  -  |
**502** | The provider failed; any tokens spent were refunded unless &#x60;refund&#x60; says otherwise |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_generate_speech_post**
> GenerateSpeechResponse v1_generate_speech_post(generate_speech_request)

Generate speech from text (25 tokens per 1,000 characters)

Narration-quality text to speech (ElevenLabs multilingual, 29 languages; the same voice reads every language, so a re-voice keeps the narrator). Billed per character of `text`, pro rata, spent before the call and refunded on provider failure. Rate limited to 30/min. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.generate_speech_request import GenerateSpeechRequest
from ffmpeg_micro.models.generate_speech_response import GenerateSpeechResponse
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    generate_speech_request = ffmpeg_micro.GenerateSpeechRequest() # GenerateSpeechRequest | 

    try:
        # Generate speech from text (25 tokens per 1,000 characters)
        api_response = api_instance.v1_generate_speech_post(generate_speech_request)
        print("The response of DefaultApi->v1_generate_speech_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_generate_speech_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_speech_request** | [**GenerateSpeechRequest**](GenerateSpeechRequest.md)|  | 

### Return type

[**GenerateSpeechResponse**](GenerateSpeechResponse.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Speech generated |  -  |
**400** | Invalid input (charged nothing) |  -  |
**401** | Missing/invalid API key |  -  |
**402** | Not enough tokens for this call; nothing was charged (for &#x60;animate&#x60;, &#x60;id&#x60; and &#x60;cancelled&#x60; are present if a render had already been submitted) |  -  |
**429** | Per-API-key rate limit exceeded (free routes 60/min, paid routes 30/min); see &#x60;x-ratelimit-*&#x60; headers |  -  |
**502** | The provider failed; any tokens spent were refunded unless &#x60;refund&#x60; says otherwise |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_generate_translate_post**
> GenerateTranslateResponse v1_generate_translate_post(generate_translate_request)

Translate an ordered list of narrations (free)

Translate scene narrations into another language, preserving count and order, so the images built for the source language can be reused and a re-voice costs speech tokens only. Free; rate limited to 60/min per key. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.generate_translate_request import GenerateTranslateRequest
from ffmpeg_micro.models.generate_translate_response import GenerateTranslateResponse
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    generate_translate_request = ffmpeg_micro.GenerateTranslateRequest() # GenerateTranslateRequest | 

    try:
        # Translate an ordered list of narrations (free)
        api_response = api_instance.v1_generate_translate_post(generate_translate_request)
        print("The response of DefaultApi->v1_generate_translate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_generate_translate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_translate_request** | [**GenerateTranslateRequest**](GenerateTranslateRequest.md)|  | 

### Return type

[**GenerateTranslateResponse**](GenerateTranslateResponse.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Translations, same length and order as &#x60;texts&#x60; |  -  |
**400** | Invalid input |  -  |
**401** | Missing/invalid API key |  -  |
**429** | Per-API-key rate limit exceeded (free routes 60/min, paid routes 30/min); see &#x60;x-ratelimit-*&#x60; headers |  -  |
**502** | The provider failed; any tokens spent were refunded unless &#x60;refund&#x60; says otherwise |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transcodes_get**
> V1TranscodesGet200Response v1_transcodes_get(status=status, page=page, limit=limit, order=order, job_type=job_type, since=since, until=until)

List transcodes (for the authenticated user)

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.transcode_status import TranscodeStatus
from ffmpeg_micro.models.v1_transcodes_get200_response import V1TranscodesGet200Response
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    status = ffmpeg_micro.TranscodeStatus() # TranscodeStatus | Filter by status. The value is not validated against the enum — an unknown value returns an empty result set, not an error.  (optional)
    page = 1 # int |  (optional) (default to 1)
    limit = 10 # int | Values outside 1-100 are clamped; non-numeric values return 400 (optional) (default to 10)
    order = created_at.desc # str | Result ordering. Use `updated_at.asc` for cursor-based polling so the sort matches the `since` filter (both key on `updated_at`); paging forward with the default `created_at.desc` skips backlog items. Use `updated_at.desc` for a newest-first view on the same cursor column (for example, choosing where a poller starts). Unknown values return 400.  (optional) (default to created_at.desc)
    job_type = 'job_type_example' # str | Restrict to one job type. Without it this endpoint returns BOTH transcode and transcribe jobs (they share the resource shape).  (optional)
    since = '2013-10-20T19:20:30+01:00' # datetime | Return transcodes last updated at/after this timestamp (filters on `updated_at`, not `created_at` — a job created earlier but completed inside the window is included). Invalid dates are rejected with 400.  (optional)
    until = '2013-10-20T19:20:30+01:00' # datetime | Return transcodes last updated at/before this timestamp (filters on `updated_at`) (optional)

    try:
        # List transcodes (for the authenticated user)
        api_response = api_instance.v1_transcodes_get(status=status, page=page, limit=limit, order=order, job_type=job_type, since=since, until=until)
        print("The response of DefaultApi->v1_transcodes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transcodes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**TranscodeStatus**](.md)| Filter by status. The value is not validated against the enum — an unknown value returns an empty result set, not an error.  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**| Values outside 1-100 are clamped; non-numeric values return 400 | [optional] [default to 10]
 **order** | **str**| Result ordering. Use &#x60;updated_at.asc&#x60; for cursor-based polling so the sort matches the &#x60;since&#x60; filter (both key on &#x60;updated_at&#x60;); paging forward with the default &#x60;created_at.desc&#x60; skips backlog items. Use &#x60;updated_at.desc&#x60; for a newest-first view on the same cursor column (for example, choosing where a poller starts). Unknown values return 400.  | [optional] [default to created_at.desc]
 **job_type** | **str**| Restrict to one job type. Without it this endpoint returns BOTH transcode and transcribe jobs (they share the resource shape).  | [optional] 
 **since** | **datetime**| Return transcodes last updated at/after this timestamp (filters on &#x60;updated_at&#x60;, not &#x60;created_at&#x60; — a job created earlier but completed inside the window is included). Invalid dates are rejected with 400.  | [optional] 
 **until** | **datetime**| Return transcodes last updated at/before this timestamp (filters on &#x60;updated_at&#x60;) | [optional] 

### Return type

[**V1TranscodesGet200Response**](V1TranscodesGet200Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK (total count is in the body &#x60;total&#x60; field) |  -  |
**400** | Invalid page, limit, since, or until parameter |  -  |
**401** | Missing/invalid API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transcodes_id_cancel_patch**
> V1TranscodesIdCancelPatch200Response v1_transcodes_id_cancel_patch(id)

Cancel a transcode job

Cancels a transcode job that is currently `pending` or `processing`. Completed, failed, or already-canceled jobs cannot be cancelled and return 400. If the job has been handed off to the toolkit service, a best-effort cancel is also sent to the toolkit — failures there are logged but do not fail this request. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.v1_transcodes_id_cancel_patch200_response import V1TranscodesIdCancelPatch200Response
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Cancel a transcode job
        api_response = api_instance.v1_transcodes_id_cancel_patch(id)
        print("The response of DefaultApi->v1_transcodes_id_cancel_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transcodes_id_cancel_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1TranscodesIdCancelPatch200Response**](V1TranscodesIdCancelPatch200Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job cancelled successfully |  -  |
**400** | Job is not in a cancellable state |  -  |
**401** | Missing/invalid API key |  -  |
**404** | Resource not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transcodes_id_download_get**
> V1TranscodesIdDownloadGet200Response v1_transcodes_id_download_get(id)

Get a signed download URL for a completed transcode

Returns a short-lived (10 minute) signed HTTPS URL for the completed output file. Because `output_url` on the transcode resource is a `gs://` URL that cannot be fetched directly by HTTP clients, use this endpoint to obtain a fetchable URL. The client is then responsible for downloading the file directly from the returned URL — the gateway does not proxy file bytes. The job must be in `completed` status and have a non-null `output_url`. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.v1_transcodes_id_download_get200_response import V1TranscodesIdDownloadGet200Response
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a signed download URL for a completed transcode
        api_response = api_instance.v1_transcodes_id_download_get(id)
        print("The response of DefaultApi->v1_transcodes_id_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transcodes_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1TranscodesIdDownloadGet200Response**](V1TranscodesIdDownloadGet200Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signed HTTPS URL valid for 10 minutes |  -  |
**400** | Transcode not completed or has no output |  -  |
**401** | Missing/invalid API key |  -  |
**404** | Resource not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transcodes_id_get**
> Transcode v1_transcodes_id_get(id)

Get a transcode

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.transcode import Transcode
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a transcode
        api_response = api_instance.v1_transcodes_id_get(id)
        print("The response of DefaultApi->v1_transcodes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transcodes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Transcode**](Transcode.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Missing/invalid API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transcodes_post**
> V1TranscodesPost201Response v1_transcodes_post(create_transcode_request)

Create a transcode or multi-video composition

Queues a new transcode job with support for single or multiple inputs. Supports simple presets (quality/resolution) or advanced mode (raw FFmpeg options). Billing is based on total input duration (sum of all inputs). Returns a short acknowledgement with `status=pending`; poll `GET /v1/transcodes/{id}` for the full resource. Quota and plan limits (processing minutes, max input file size) are checked asynchronously after the 201: a job that exceeds them transitions to `failed` with an explanatory `error_message` and `error_category` (`quota` or `file_size`) instead of an HTTP error. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.create_transcode_request import CreateTranscodeRequest
from ffmpeg_micro.models.v1_transcodes_post201_response import V1TranscodesPost201Response
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    create_transcode_request = {"inputs":[{"url":"https://cdn.pixabay.com/video/2021/05/22/74779-554220620_large.mp4"}],"outputFormat":"mp4","preset":{"quality":"high","resolution":"1080p"}} # CreateTranscodeRequest | 

    try:
        # Create a transcode or multi-video composition
        api_response = api_instance.v1_transcodes_post(create_transcode_request)
        print("The response of DefaultApi->v1_transcodes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transcodes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transcode_request** | [**CreateTranscodeRequest**](CreateTranscodeRequest.md)|  | 

### Return type

[**V1TranscodesPost201Response**](V1TranscodesPost201Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Invalid input |  -  |
**401** | Missing/invalid API key |  -  |
**402** | The account is fully capped: zero plan minutes remaining AND a zero token balance, so no job of any size can run until the plan renews, the plan is upgraded, or tokens are topped up. Returned synchronously instead of a &#x60;201&#x60; — no processing is attempted. A job record IS still created (visible in job listings with &#x60;status: failed&#x60;), and its id is returned so the blocked attempt can be inspected. Automations should treat &#x60;402&#x60; as terminal for the billing period and STOP retrying: the same request will keep returning &#x60;402&#x60; until the account&#39;s quota state changes. Partially-capped accounts (some minutes or tokens remaining) still return &#x60;201&#x60;, with any quota failure reported asynchronously on the job&#39;s &#x60;status&#x60;/&#x60;error_message&#x60;.  |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transcribe_id_download_get**
> V1TranscribeIdDownloadGet200Response v1_transcribe_id_download_get(id)

Get a signed download URL for the generated SRT

Returns a short-lived (10 minute) signed HTTPS URL for the completed SRT file. The job must be in `completed` status. 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.v1_transcribe_id_download_get200_response import V1TranscribeIdDownloadGet200Response
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a signed download URL for the generated SRT
        api_response = api_instance.v1_transcribe_id_download_get(id)
        print("The response of DefaultApi->v1_transcribe_id_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transcribe_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1TranscribeIdDownloadGet200Response**](V1TranscribeIdDownloadGet200Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signed HTTPS URL valid for 10 minutes |  -  |
**400** | Transcribe not completed or has no output |  -  |
**401** | Missing/invalid API key |  -  |
**404** | Resource not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transcribe_id_get**
> Transcribe v1_transcribe_id_get(id)

Get transcribe job status

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.transcribe import Transcribe
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get transcribe job status
        api_response = api_instance.v1_transcribe_id_get(id)
        print("The response of DefaultApi->v1_transcribe_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transcribe_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Transcribe**](Transcribe.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transcribe job details |  -  |
**401** | Missing/invalid API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transcribe_post**
> TranscribeCreated v1_transcribe_post(create_transcribe_request)

Create a transcribe job (audio → SRT)

Generate an SRT subtitle file from an audio or video URL using Whisper. Returns a short acknowledgement with `status=pending`; poll `GET /v1/transcribe/{id}` until `status` is `completed`, then fetch the SRT via `GET /v1/transcribe/{id}/download`. The resulting SRT is stored in your user-namespaced output bucket and can be referenced inside a transcode `subtitles=` filter to burn captions into a video (see the docs for the zoom+captions tutorial). 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.create_transcribe_request import CreateTranscribeRequest
from ffmpeg_micro.models.transcribe_created import TranscribeCreated
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    create_transcribe_request = ffmpeg_micro.CreateTranscribeRequest() # CreateTranscribeRequest | 

    try:
        # Create a transcribe job (audio → SRT)
        api_response = api_instance.v1_transcribe_post(create_transcribe_request)
        print("The response of DefaultApi->v1_transcribe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transcribe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transcribe_request** | [**CreateTranscribeRequest**](CreateTranscribeRequest.md)|  | 

### Return type

[**TranscribeCreated**](TranscribeCreated.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transcribe job created |  -  |
**400** | Invalid input (missing or invalid &#x60;media_url&#x60;) |  -  |
**401** | Missing/invalid API key |  -  |
**402** | The account is fully capped: zero plan minutes remaining AND a zero token balance, so no job of any size can run until the plan renews, the plan is upgraded, or tokens are topped up. Returned synchronously instead of a &#x60;201&#x60; — no processing is attempted. A job record IS still created (visible in job listings with &#x60;status: failed&#x60;), and its id is returned so the blocked attempt can be inspected. Automations should treat &#x60;402&#x60; as terminal for the billing period and STOP retrying: the same request will keep returning &#x60;402&#x60; until the account&#39;s quota state changes. Partially-capped accounts (some minutes or tokens remaining) still return &#x60;201&#x60;, with any quota failure reported asynchronously on the job&#39;s &#x60;status&#x60;/&#x60;error_message&#x60;.  |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_transcribes_get**
> V1TranscribesGet200Response v1_transcribes_get(status=status, page=page, limit=limit, order=order, since=since, until=until)

List transcribe jobs (for the authenticated user)

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.transcode_status import TranscodeStatus
from ffmpeg_micro.models.v1_transcribes_get200_response import V1TranscribesGet200Response
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    status = ffmpeg_micro.TranscodeStatus() # TranscodeStatus | Filter by status. The value is not validated against the enum — an unknown value returns an empty result set, not an error.  (optional)
    page = 1 # int |  (optional) (default to 1)
    limit = 10 # int | Values outside 1-100 are clamped; non-numeric values return 400 (optional) (default to 10)
    order = created_at.desc # str | Result ordering. Use `updated_at.asc` for cursor-based polling so the sort matches the `since` filter, or `updated_at.desc` for a newest-first view on the same cursor column. Unknown values return 400.  (optional) (default to created_at.desc)
    since = '2013-10-20T19:20:30+01:00' # datetime | Return transcribes last updated at/after this timestamp (filters on `updated_at`). Invalid dates are rejected with 400.  (optional)
    until = '2013-10-20T19:20:30+01:00' # datetime | Return transcribes last updated at/before this timestamp (filters on `updated_at`) (optional)

    try:
        # List transcribe jobs (for the authenticated user)
        api_response = api_instance.v1_transcribes_get(status=status, page=page, limit=limit, order=order, since=since, until=until)
        print("The response of DefaultApi->v1_transcribes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_transcribes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**TranscodeStatus**](.md)| Filter by status. The value is not validated against the enum — an unknown value returns an empty result set, not an error.  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**| Values outside 1-100 are clamped; non-numeric values return 400 | [optional] [default to 10]
 **order** | **str**| Result ordering. Use &#x60;updated_at.asc&#x60; for cursor-based polling so the sort matches the &#x60;since&#x60; filter, or &#x60;updated_at.desc&#x60; for a newest-first view on the same cursor column. Unknown values return 400.  | [optional] [default to created_at.desc]
 **since** | **datetime**| Return transcribes last updated at/after this timestamp (filters on &#x60;updated_at&#x60;). Invalid dates are rejected with 400.  | [optional] 
 **until** | **datetime**| Return transcribes last updated at/before this timestamp (filters on &#x60;updated_at&#x60;) | [optional] 

### Return type

[**V1TranscribesGet200Response**](V1TranscribesGet200Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid page, limit, since, or until parameter |  -  |
**401** | Missing/invalid API key |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_upload_confirm_post**
> V1UploadConfirmPost200Response v1_upload_confirm_post(v1_upload_confirm_post_request)

Confirm file upload

Confirms that a file has been successfully uploaded to GCS. This is the final step in the upload workflow. **Use the returned GCS URL in your transcode requests:** - Format: `gs://bucket-name/filename` - Example: `gs://<YOUR_BUCKET>/20251023-143045-my-video.mp4` 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.v1_upload_confirm_post200_response import V1UploadConfirmPost200Response
from ffmpeg_micro.models.v1_upload_confirm_post_request import V1UploadConfirmPostRequest
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    v1_upload_confirm_post_request = {"filename":"20251023-143045-my-video.mp4","fileSize":10485760,"uploadId":"upload-12345"} # V1UploadConfirmPostRequest | 

    try:
        # Confirm file upload
        api_response = api_instance.v1_upload_confirm_post(v1_upload_confirm_post_request)
        print("The response of DefaultApi->v1_upload_confirm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_upload_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_upload_confirm_post_request** | [**V1UploadConfirmPostRequest**](V1UploadConfirmPostRequest.md)|  | 

### Return type

[**V1UploadConfirmPost200Response**](V1UploadConfirmPost200Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload confirmed successfully |  -  |
**400** | Bad Request |  -  |
**401** | Missing/invalid API key |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_upload_presigned_url_post**
> V1UploadPresignedUrlPost200Response v1_upload_presigned_url_post(v1_upload_presigned_url_post_request)

Generate presigned upload URL

Generates a presigned URL for direct file upload to Google Cloud Storage. This is the first step in the upload workflow - use the returned URL to upload your file. **Upload Workflow:** 1. Call this endpoint to get a presigned URL 2. Upload file directly to GCS using HTTP PUT 3. Call `/v1/upload/confirm` to verify upload 4. Use the GCS URL in your transcode request **Benefits:** - No server bandwidth usage - Faster uploads (direct to GCS) - Secure (presigned URLs expire) 

### Example

* Bearer (opaque-api-key) Authentication (bearerApiKey):

```python
import ffmpeg_micro
from ffmpeg_micro.models.v1_upload_presigned_url_post200_response import V1UploadPresignedUrlPost200Response
from ffmpeg_micro.models.v1_upload_presigned_url_post_request import V1UploadPresignedUrlPostRequest
from ffmpeg_micro.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ffmpeg-micro.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ffmpeg_micro.Configuration(
    host = "https://api.ffmpeg-micro.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque-api-key): bearerApiKey
configuration = ffmpeg_micro.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with ffmpeg_micro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ffmpeg_micro.DefaultApi(api_client)
    v1_upload_presigned_url_post_request = {"filename":"my-video.mp4","contentType":"video/mp4","fileSize":10485760} # V1UploadPresignedUrlPostRequest | 

    try:
        # Generate presigned upload URL
        api_response = api_instance.v1_upload_presigned_url_post(v1_upload_presigned_url_post_request)
        print("The response of DefaultApi->v1_upload_presigned_url_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v1_upload_presigned_url_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_upload_presigned_url_post_request** | [**V1UploadPresignedUrlPostRequest**](V1UploadPresignedUrlPostRequest.md)|  | 

### Return type

[**V1UploadPresignedUrlPost200Response**](V1UploadPresignedUrlPost200Response.md)

### Authorization

[bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Presigned URL generated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Missing/invalid API key |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

