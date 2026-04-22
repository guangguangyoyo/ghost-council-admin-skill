#!/usr/bin/env python3
import sys
from common import request_json, print_json, resolve_admin_token, resolve_base_url

if len(sys.argv) not in (1, 2, 3, 4):
    raise SystemExit('Usage: run_cycle.py [base_url] [admin_token] [count]')
base = resolve_base_url(sys.argv[1] if len(sys.argv) >= 2 else None)
token = resolve_admin_token(sys.argv[2] if len(sys.argv) >= 3 else None)
count = int(sys.argv[3]) if len(sys.argv) >= 4 else 1
headers = {'X-Admin-Token': token}
out = []
for _ in range(count):
    out.append(request_json(base + '/api/admin/run-cycle', method='POST', headers=headers))
print_json(out if count != 1 else out[0])
