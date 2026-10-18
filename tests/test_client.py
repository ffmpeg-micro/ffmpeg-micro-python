"""Offline checks: the client builds the request the API expects."""
import ffmpeg_micro
from ffmpeg_micro.models import CreateTranscodeRequest


def api():
    config = ffmpeg_micro.Configuration(access_token="test-key")
    return ffmpeg_micro.DefaultApi(ffmpeg_micro.ApiClient(config))


def test_create_transcode_request_shape():
    body = CreateTranscodeRequest.from_dict({
        "inputs": [{"url": "https://example.com/in.mov"}],
        "outputFormat": "mp4",
        "preset": {"quality": "high", "resolution": "1080p"},
    })
    method, url, headers, payload, _ = api()._v1_transcodes_post_serialize(
        body, None, None, None, 0)
    assert method == "POST"
    assert url == "https://api.ffmpeg-micro.com/v1/transcodes"
    assert headers["Authorization"] == "Bearer test-key"
    assert payload == {"inputs": [{"url": "https://example.com/in.mov"}],
                       "outputFormat": "mp4",
                       "preset": {"quality": "high", "resolution": "1080p"}}


def test_path_parameters_are_filled():
    method, url, *_ = api()._v1_transcodes_id_get_serialize("abc", None, None, None, 0)
    assert (method, url) == ("GET", "https://api.ffmpeg-micro.com/v1/transcodes/abc")
