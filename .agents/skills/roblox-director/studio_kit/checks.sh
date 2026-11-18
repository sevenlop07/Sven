#!/bin/bash
# Legacy wrapper: delegates to cross-platform checks.py
cd "$(dirname "$0")"
python checks.py "$@"
