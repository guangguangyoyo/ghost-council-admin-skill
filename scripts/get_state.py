#!/usr/bin/env python3
import sys
from common import request_json, print_json, resolve_base_url

if len(sys.argv) not in (1, 2):
    raise SystemExit('Usage: get_state.py [base_url]')
base = resolve_base_url(sys.argv[1] if len(sys.argv) == 2 else None)
print_json(request_json(base + '/api/state'))
