# FFmpeg Micro for Python

The official Python client for the [FFmpeg Micro](https://www.ffmpeg-micro.com) API. FFmpeg Micro runs FFmpeg in the cloud: transcode and compress video, stitch clips, add text overlays, extract audio, generate thumbnails and transcribe speech through one API. There are no servers to manage and no FFmpeg builds to maintain.

```bash
pip install ffmpeg-micro
```

## Quickstart

Get an API key from the [FFmpeg Micro dashboard](https://www.ffmpeg-micro.com). The free plan needs no credit card.

```python
import os
import time

import ffmpeg_micro
from ffmpeg_micro.models import CreateTranscodeRequest

config = ffmpeg_micro.Configuration(access_token=os.environ["FFMPEG_MICRO_API_KEY"])

with ffmpeg_micro.ApiClient(config) as client:
    api = ffmpeg_micro.DefaultApi(client)

    job = api.v1_transcodes_post(CreateTranscodeRequest.from_dict({
        "inputs": [{"url": "https://example.com/input.mov"}],
        "outputFormat": "mp4",
        "preset": {"quality": "high", "resolution": "1080p"},
    }))

    while api.v1_transcodes_id_get(job.id).status not in ("completed", "failed", "canceled"):
        time.sleep(5)

    print(api.v1_transcodes_id_download_get(job.id).url)
```

Inputs can be public HTTP(S) URLs or files you upload first with `v1_upload_presigned_url_post` and `v1_upload_confirm_post`.

## What it covers

Every endpoint in the [FFmpeg Micro API](https://www.ffmpeg-micro.com/docs):

- Transcodes: create, list, get, cancel and download jobs, including multi-video compositions, raw FFmpeg options and `@text-overlay`
- Uploads of your own files through presigned URLs
- FFprobe media metadata for any input
- Transcription of speech to text, with downloadable results
- Blueprints, which are ready-made multi-step video pipelines
- Generate endpoints for scenes, translation, images, speech and animation

Each method and model is documented in [`docs/`](docs/). Method names follow the HTTP route (`v1_transcodes_post` is `POST /v1/transcodes`).

## Notes

- `Transcode.inputs[].size_bytes` is a decimal string on current jobs (`"991017"`), as the API returns it. The client exposes it as a wrapper; read `size_bytes.actual_instance` and convert with `int(...)`.
- Job status values are `pending`, `processing`, `completed`, `failed` and `canceled`.

## Errors

Failed calls raise `ffmpeg_micro.ApiException` (subclasses include `UnauthorizedException`, `NotFoundException` and `ServiceException`). The exception's `status` and `body` carry the API's error response.

## How it is built

The client is generated with [OpenAPI Generator](https://openapi-generator.tech) from the [OpenAPI spec](https://api.ffmpeg-micro.com/openapi.yaml) the API itself serves, so it always matches the live API. `./generate.sh` regenerates it.

## Links

- Website: https://www.ffmpeg-micro.com
- API docs: https://www.ffmpeg-micro.com/docs
- OpenAPI spec: https://api.ffmpeg-micro.com/openapi.yaml

MIT licensed.
