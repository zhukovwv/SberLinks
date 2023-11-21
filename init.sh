#!/bin/bash
set -x

echo "Run migrations"
alembic upgrade head