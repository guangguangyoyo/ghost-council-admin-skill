#!/usr/bin/env python3
import sys
from common import request_json, print_json

if len(sys.argv) != 4:
    raise SystemExit('Usage: set_auto_mode.py <base_url> <admin_token> <on|off>')
base = sys.argv[1].rstrip('/')
token = sys.argv[2]
mode = sys.argv[3].lower()
if mode not in ('on', 'off'):
    raise SystemExit('mode must be on or off')
headers = {'X-Admin-Token': token}
print_json(request_json(base + '/api/admin/settings', method='POST', headers=headers, payload={
    'auto_mode': mode == 'on',
}))
