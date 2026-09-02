#!/bin/bash
#
# Execute unit tests.

TEST_TYPE=${1:-"unit"}

set -e

case "$TEST_TYPE" in
  unit)
    markers="unit"
    ;;
  integration)
    markers="integration"
    ;;
  all)
    markers="unit or integration"
    ;;
  *)
    echo "Unknown test type: $TEST_TYPE"
    exit 1
    ;;
esac

echo "Executing Tests..."
uv run coverage run -m pytest -m "$markers" tui/tests/

echo "Generating Report..."
uv run coverage report -m

echo "Build HTML Report..."
uv run coverage html
