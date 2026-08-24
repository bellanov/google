#!/bin/bash
#
# Format Code Base.

echo "Formatting imports..."
isort tui

echo "Formatting code base..."
black --target-version py314 tui 
