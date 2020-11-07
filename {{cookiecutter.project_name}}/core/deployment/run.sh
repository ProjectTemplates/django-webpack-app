#! /usr/bin/env bash
set -e

python pre_start.py

export GUNICORN_CONF=${GUNICORN_CONF:-gunicorn_conf.py}
exec gunicorn -c "$GUNICORN_CONF" "$APP_MODULE"
