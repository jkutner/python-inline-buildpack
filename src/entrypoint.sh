#!/bin/bash
uv run python src/python_healthcheck.py &
p1=$!
uv run python src/python_app.py

[ "$?" -gt 1 ] || kill "$p1"
wait