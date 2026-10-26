#!/usr/bin/env python3
"""Assemble scenes.py from the user's installed Brutalist iso_kit and original body scenes.

Run in the reel folder, e.g.
  python3 assemble_scenes.py

This ensures the official iso kit is pasted into one standalone scenes.py, as
required by Brutalist's Gate A static scene check. It never modifies the toolkit.
"""
from pathlib import Path
import ast
import json

HERE = Path(__file__).resolve().parent
TOOLKIT = Path.home() / 'Documents' / 'INFO7375' / 'brutalist.art'
KIT = TOOLKIT / 'skills' / 'make' / 'show-tell' / 'templates' / 'iso_kit.py'
BODY = HERE / 'scenes_body.py'
SHEET = HERE / 'beat_sheet.json'
OUT = HERE / 'scenes.py'

if not KIT.is_file():
    raise SystemExit('Official Brutalist iso_kit.py not found: ' + str(KIT) + '\nUpdate TOOLKIT in assemble_scenes.py if Brutalist is elsewhere.')
if not BODY.is_file() or not SHEET.is_file():
    raise SystemExit('Missing scenes_body.py or beat_sheet.json: place all files in same reel folder.')

sheet = json.loads(SHEET.read_text(encoding='utf-8'))
expected = [b['shot']['manim']['class'] for b in sheet['beats'] if b.get('lane') == 'manim']
body = BODY.read_text(encoding='utf-8')
ast.parse(body)
for name in expected:
    if f'class {name}(Scene):' not in body:
        raise SystemExit(f'Missing scene class {name} in scenes_body.py')

combined = KIT.read_text(encoding='utf-8').rstrip() + '\n\n' + body
ast.parse(combined)
OUT.write_text(combined, encoding='utf-8')
print(f'Created {OUT} with {len(expected)} Manim scene classes. ({OUT.stat().st_size:,} bytes)')
print('Next: render ONE test scene at low resolution before running the full pipeline.')
