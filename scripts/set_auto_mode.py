#!/usr/bin/env python3
import sys
from common import request_json, print_json, resolve_admin_token, resolve_base_url

if len(sys.argv) not in (2, 3, 4):
    raise SystemExit('Usage: set_auto_mode.py [base_url] [admin_token] <on|off>')
if len(sys.argv) == 2:
    base = resolve_base_url()
    token = resolve_admin_token()
    mode = sys.argv[1].lower()
elif len(sys.argv) == 3:
    base = resolve_base_url(sys.argv[1])
    token = resolve_admin_token()
    mode = sys.argv[2].lower()
else:
    base = resolve_base_url(sys.argv[1])
    token = resolve_admin_token(sys.argv[2])
    mode = sys.argv[3].lower()
if mode not in ('on', 'off'):
    raise SystemExit('mode must be on or off')
headers = {'X-Admin-Token': token}
print_json(request_json(base + '/api/admin/settings', method='POST', headers=headers, payload={
    'auto_mode': mode == 'on',
}))
