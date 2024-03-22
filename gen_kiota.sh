#!/usr/bin/env bash

curl -LO https://github.com/kubeflow/model-registry/blob/e0e89210337e8c4eb44f4da7dd3f6131831ee0a1/api/openapi/model-registry.yaml

curl -LO https://github.com/microsoft/kiota/releases/download/v1.12.0/linux-x64.zip

unzip linux-x64.zip

./kiota generate -d model-registry.yaml -l python -o mr
