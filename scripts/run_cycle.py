#!/usr/bin/env python3
import sys
from common import request_json, print_json

if len(sys.argv) not in (3, 4):
    raise SystemExit('Usage: run_cycle.py <base_url> <admin_token> [count]')
base = sys.argv[1].rstrip('/')
token = sys.argv[2]
count = int(sys.argv[3]) if len(sys.argv) == 4 else 1
headers = {'X-Admin-Token': token}
out = []
for _ in range(count):
    out.append(request_json(base + '/api/admin/run-cycle', method='POST', headers=headers))
print_json(out if count != 1 else out[0])
