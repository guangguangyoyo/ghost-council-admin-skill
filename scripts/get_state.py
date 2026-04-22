#!/usr/bin/env python3
import sys
from common import request_json, print_json

if len(sys.argv) != 2:
    raise SystemExit('Usage: get_state.py <base_url>')
base = sys.argv[1].rstrip('/')
print_json(request_json(base + '/api/state'))
