#!/usr/bin/env python3
"""Dependency-free static checks for Rajasthan Routes."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
HTML_FILE = SITE / 'index.html'

class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.duplicates = set()
        self.local_refs = set()
        self.inline_scripts = []
        self._script = False
        self._external_script = False
        self._script_parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        node_id = attrs.get('id')
        if node_id:
            if node_id in self.ids:
                self.duplicates.add(node_id)
            self.ids.add(node_id)
        if tag == 'script':
            self._script = True
            self._external_script = bool(attrs.get('src'))
            self._script_parts = []
            if attrs.get('src'):
                self.local_refs.add(attrs['src'])
        for key in ('href',):
            ref = attrs.get(key, '')
            if ref and not ref.startswith(('#', 'http://', 'https://', 'mailto:', 'tel:', 'javascript:')):
                self.local_refs.add(ref)

    def handle_data(self, data):
        if self._script and not self._external_script:
            self._script_parts.append(data)

    def handle_endtag(self, tag):
        if tag == 'script' and self._script:
            if not self._external_script:
                source = ''.join(self._script_parts).strip()
                if source:
                    self.inline_scripts.append(source)
            self._script = False
            self._external_script = False
            self._script_parts = []

def fail(message):
    print('FAIL:', message)
    sys.exit(1)

if not HTML_FILE.is_file():
    fail('site/index.html is missing')
root_entry = ROOT / 'index.html'
if not root_entry.is_file():
    fail('root index.html is missing; Pages would fall back to README.md')
root_source = root_entry.read_text(encoding='utf-8')
if 'window.location.replace(target)' not in root_source or 'var target = base + "site/" + window.location.search + window.location.hash;' not in root_source or 'href="./site/"' not in root_source:
    fail('root index must forward visitors to the travel app and preserve query/anchor links')
root_parser = SiteParser()
root_parser.feed(root_source)
root_parser.close()
for i, script in enumerate(root_parser.inline_scripts, start=1):
    result = subprocess.run(['node', '--check'], input=script, text=True, capture_output=True)
    if result.returncode:
        fail('root redirect JavaScript syntax error (block ' + str(i) + '): ' + result.stderr.strip())
if not (ROOT / '.nojekyll').is_file():
    fail('root .nojekyll is missing')
source = HTML_FILE.read_text(encoding='utf-8')
parser = SiteParser()
parser.feed(source)
parser.close()
if parser.duplicates:
    fail('duplicate HTML IDs: ' + ', '.join(sorted(parser.duplicates)))

required_ids = {
    'destinations', 'route', 'days', 'people', 'daily', 'search',
    'routeKm', 'transferLegs', 'travelLoad', 'routeAdvice', 'lensOutput',
    'budgetBar', 'budgetAmounts', 'checklist', 'timeline', 'planner', 'itineraryCopy', 'itinerarySummary', 'exportDraft', 'importDraftBtn', 'importDraftFile', 'shareBtn', 'startDate', 'endDate', 'dateNotice',
}
missing = required_ids - parser.ids
if missing:
    fail('required UI IDs missing: ' + ', '.join(sorted(missing)))

for ref in sorted(parser.local_refs):
    if ref.startswith('#') or not ref:
        continue
    clean = ref.split('#', 1)[0].split('?', 1)[0]
    if not clean:
        continue
    target = (SITE / clean).resolve()
    if not target.exists():
        fail('local asset link is broken: ' + ref)

if not (ROOT / 'scripts' / 'browser_site.cjs').is_file():
    fail('Chromium browser test script is missing')
if not (ROOT / 'scripts' / 'smoke_site.cjs').is_file():
    fail('DOM smoke test script is missing')
for script in sorted((SITE / 'trip-intelligence.js', SITE / 'itinerary.js', SITE / 'sw.js')):
    if not script.is_file():
        fail('required JavaScript file missing: ' + str(script.relative_to(ROOT)))
    result = subprocess.run(['node', '--check'], input=script.read_text(encoding='utf-8'), text=True, capture_output=True)
    if result.returncode:
        fail('JavaScript syntax error in ' + str(script.relative_to(ROOT)) + ': ' + result.stderr.strip())

for i, script in enumerate(parser.inline_scripts, start=1):
    result = subprocess.run(['node', '--check'], input=script, text=True, capture_output=True)
    if result.returncode:
        fail('inline JavaScript syntax error (block ' + str(i) + '): ' + result.stderr.strip())

try:
    manifest = json.loads((SITE / 'manifest.webmanifest').read_text(encoding='utf-8'))
except Exception as exc:
    fail('manifest is invalid JSON: ' + str(exc))
for key in ('name', 'short_name', 'start_url', 'scope', 'icons'):
    if key not in manifest:
        fail('manifest field missing: ' + key)

required_features = ('data-filter', 'data-add', 'data-remove', 'data-up', 'serviceWorker.register', 'navigator.clipboard', 'itinerary.js', 'trip-intelligence.js', 'rajasthan-trip-backup.json', 'importDraftFile', 'syncTripDates', 'startDate', 'endDate', 'type="date"', 'data-nights', 'nightsByStop')
for feature in required_features:
    if feature not in source:
        fail('expected feature hook is missing from index.html: ' + feature)

print('PASS: repository-root entry forwards Pages visitors to the travel app.')
print('PASS: HTML IDs are unique and required planner controls exist.')
print('PASS: all local links and app assets resolve.')
print('PASS: inline JavaScript, trip-intelligence.js, and sw.js parse successfully.')
print('PASS: web app manifest is valid JSON with required fields.')
print('PASS: core filter, itinerary, clipboard, and offline hooks are present.')