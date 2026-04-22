#!/usr/bin/env python3
import sys
from common import request_json, print_json, resolve_admin_token, resolve_base_url

if len(sys.argv) not in (3, 4, 5):
    raise SystemExit('Usage: create_topic.py [base_url] [admin_token] <title> <seed>')
if len(sys.argv) == 3:
    base = resolve_base_url()
    token = resolve_admin_token()
    title = sys.argv[1]
    seed = sys.argv[2]
elif len(sys.argv) == 4:
    base = resolve_base_url(sys.argv[1])
    token = resolve_admin_token()
    title = sys.argv[2]
    seed = sys.argv[3]
else:
    base = resolve_base_url(sys.argv[1])
    token = resolve_admin_token(sys.argv[2])
    title = sys.argv[3]
    seed = sys.argv[4]
headers = {'X-Admin-Token': token}
print_json(request_json(base + '/api/admin/topic', method='POST', headers=headers, payload={
    'title': title,
    'seed': seed,
}))
