#! /usr/bin/env bash
set -e

echo "Building for run level '${RUN_LEVEL}'"
poetry install $(if [ "${RUN_LEVEL}" == "production" ]; then echo "--no-dev"; fi ) --no-interaction --no-ansi
