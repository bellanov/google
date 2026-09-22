#!/bin/bash
#
# Format Code Base.

echo "Formatting imports..."
uv run isort tui

echo "Formatting code base..."
uv run black --target-version py314 tui 
