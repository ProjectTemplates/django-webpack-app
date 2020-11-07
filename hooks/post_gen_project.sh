#!/usr/bin/env bash
set -e
cd core

mkdir dist

cp .env.example .env
echo "Copied default .env.example to .env"
