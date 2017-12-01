#!/usr/bin/env python3
"""
Download CodeRegation proposal from GitHub and convert to blogpost.

Usage: see command line help.
"""
import requests
import json
import argparse
import datetime
import pathlib

def last_wednesday():
    today = datetime.date.today()
    offset = (today.weekday() - 2) % 7
    day = today - datetime.timedelta(days=offset)
    return day.strftime('%Y-%m-%d')

parser = argparse.ArgumentParser(description='Download CodeRegation proposal from GitHub and convert to blogpost.')
parser.add_argument('--id', help='GitHub issue id', required=True)
parser.add_argument('--date', help='Date of CodeRegation meeting. Default: last Wednesday.', default=last_wednesday())
args = parser.parse_args()

issue_id = args.id
date = args.date

response = requests.get(url=f'https://api.github.com/repos/balabit/coderegation/issues/{issue_id}')
data = response.json()
description = data['body']
print(f'Preparing "{data["title"]}" at "{date}"')

new_item = pathlib.Path(__file__).with_name('new_item.md')

with new_item.open('w') as f:
    f.write(f'date: {date}\n')
    f.write(f'issue:  {issue_id}\n')
    f.write(description)

print('-----------------------------------------------------')
print(new_item.read_text())
