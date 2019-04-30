#!/usr/bin/env python

import os
from datetime import datetime
import argparse
import requests

parser = argparse.ArgumentParser(description='Show issues closed on a week')
parser.add_argument('org', type=str, help='an organization name')
parser.add_argument('week', type=int, help='a number of week')
args = parser.parse_args()
org = args.org
week = args.week

token_file = 'token.txt'
if not os.path.exists(token_file):
    raise RuntimeError('{file} is not exists'.format(file=token_file))
if not os.path.isfile(token_file):
    raise RuntimeError('{file} is not a regular file'.format(file=token_file))
with open(token_file, 'r') as f:
    token = f.read().strip()

since = datetime.strptime('2019-W{}-1'.format(week), "%G-W%V-%w")
until = datetime.strptime('2019-W{}-1'.format(week + 1), "%G-W%V-%w")

session = requests.Session()
headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'token ' + token,
}
params = {
    'filter': 'all',
    'state': 'closed',
    'sort': 'updated',
    'since': since.isoformat(timespec='seconds'),
}
base_url = 'https://api.github.com/orgs/{}/issues'.format(org)
r = session.get(base_url, headers=headers, params=params)

data = []
data.extend(r.json())

while 'next' in r.links:
    next_url = r.links['next']['url']
    r = session.get(next_url, headers=headers)
    data.extend(r.json())

issues_per_repo = {}

for issue in data:
    closed_at = datetime.strptime(issue['closed_at'], '%Y-%m-%dT%H:%M:%SZ')
    if closed_at < since or closed_at >= until:
        continue
    number = '#' + str(issue['number'])
    if 'pull_request' in issue:
        number = 'PR ' + number
    title = issue['title'].strip()
    milestone = issue['milestone']['title'] if issue['milestone'] else None
    repo = issue['repository']['name']
    result = {
        'number': number,
        'milestone': milestone,
        'title': title,
        'repo': repo,
    }
    if repo not in issues_per_repo.keys():
        issues_per_repo[repo] = []
    issues_per_repo[repo].append(result)

for repo, issues in issues_per_repo.items():
    for issue in issues:
        if issue['milestone']:
            print('{repo}: [{number}, {milestone}] {title}'.format(**issue))
        else:
            print('{repo}: [{number}] {title}'.format(**issue))
