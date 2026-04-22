#!/usr/bin/env python3
import sys
from common import request_json, print_json, resolve_base_url, resolve_registration_command

if len(sys.argv) not in (1, 2, 3):
    raise SystemExit('Usage: register_agent.py [base_url] [registration_command]')

if len(sys.argv) == 1:
    base = resolve_base_url()
    command = resolve_registration_command()
elif len(sys.argv) == 2:
    base = resolve_base_url(sys.argv[1])
    command = resolve_registration_command()
else:
    base = resolve_base_url(sys.argv[1])
    command = resolve_registration_command(sys.argv[2])

print_json(request_json(base + '/api/register', method='POST', payload={
    'command': command,
}))
