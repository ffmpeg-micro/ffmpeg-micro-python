#!/usr/bin/env bash
# Regenerate the client from the spec production serves. There is one spec,
# the one the API serves at /openapi.yaml; nothing here keeps a copy of it.
# Only ffmpeg_micro/ and docs/ are generated; everything else is hand-written.
set -euo pipefail
cd "$(dirname "$0")"
SPEC_URL="${SPEC_URL:-https://api.ffmpeg-micro.com/openapi.yaml}"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
curl -fsS "$SPEC_URL" -o "$work/openapi.yaml"
cp generator-config.yaml "$work/"
docker run --rm -u "$(id -u):$(id -g)" -v "$work:/local" openapitools/openapi-generator-cli:v7.10.0 \
  generate -i /local/openapi.yaml -g python -c /local/generator-config.yaml -o /local/out \
  --skip-validate-spec >/dev/null
rm -rf ffmpeg_micro docs
mv "$work/out/ffmpeg_micro" "$work/out/docs" .
echo "Regenerated from $SPEC_URL"
