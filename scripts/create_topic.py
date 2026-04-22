#!/usr/bin/env python3
import sys
from common import request_json, print_json

if len(sys.argv) != 5:
    raise SystemExit('Usage: create_topic.py <base_url> <admin_token> <title> <seed>')
base = sys.argv[1].rstrip('/')
token = sys.argv[2]
title = sys.argv[3]
seed = sys.argv[4]
headers = {'X-Admin-Token': token}
print_json(request_json(base + '/api/admin/topic', method='POST', headers=headers, payload={
    'title': title,
    'seed': seed,
}))
