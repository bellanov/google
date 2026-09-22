#!/bin/bash
#
# Create Virtual Environment.

PYTHON_VERSION="3.14"

echo "Creating Virtual Environment ${PYTHON_VERSION}..."
uv venv --python ${PYTHON_VERSION}
