#!/usr/bin/env python3
import json
import os
import sys
import urllib.request
from pathlib import Path


def load_env():
    env_path = Path(__file__).resolve().parent.parent / '.env'
    if not env_path.exists():
        return
    for raw in env_path.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip()
        if key and key not in os.environ:
            os.environ[key] = value


def default_base_url():
    load_env()
    return os.environ.get('GHOST_COUNCIL_BASE_URL', '').rstrip('/')


def default_admin_token():
    load_env()
    return os.environ.get('GHOST_COUNCIL_ADMIN_TOKEN', '').strip()


def resolve_base_url(value=None):
    base = (value or default_base_url()).rstrip('/')
    if not base:
        raise SystemExit('Missing base_url. Pass it as an argument or set GHOST_COUNCIL_BASE_URL in .env')
    return base


def resolve_admin_token(value=None):
    token = (value or default_admin_token()).strip()
    if not token:
        raise SystemExit('Missing admin token. Pass it as an argument or set GHOST_COUNCIL_ADMIN_TOKEN in .env')
    return token


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
