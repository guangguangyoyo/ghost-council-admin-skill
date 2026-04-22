#!/usr/bin/env python3
import json
import sys
import urllib.request


def request_json(url, method='GET', headers=None, payload=None):
    data = None
    req_headers = {'Content-Type': 'application/json'}
    if headers:
        req_headers.update(headers)
    if payload is not None:
        data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=req_headers, method=method)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode('utf-8'))


def print_json(obj):
    sys.stdout.write(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
