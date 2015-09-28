#!/usr/bin/env pyhton
import os
import re
import string
from unidecode import unidecode

SOURCE_FILENAME = 'new_item.md'

def get_filename(headers):
    filename = '{}-{}-{}'.format(headers['date'], headers['speaker'], headers['topic'])
    filename = filename.replace(' ', '-')
    filename = filename.replace('.', '-')
    filename = filename.replace(':', '-')
    filename = unidecode(filename)
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in filename if c in valid_chars)
    filename = re.sub(r'-+', '-', filename)
    return filename + '.md'


def get_headers(in_file):
    headers = {}
    while True:
        line = next(in_file).strip()
        if line == '':
            return headers
        match = re.match(r'(.+?):\s*(.+)', line)
        headers[match.group(1)] = match.group(2)


def get_body(in_file):
    return ''.join([line for line in in_file])


def write_output(headers, body):
      with open(get_filename(headers), 'w', encoding='utf8')  as md_file:
          md_file.write('---\n')
          md_file.write('speaker: ' + headers['speaker'] + '\n')
          md_file.write('topic: ' + headers['topic'].replace(':', ' -') + '\n')
          if 'video' in headers:
              md_file.write('video: ' + headers['video'] + '\n')
          md_file.write('---\n\n')
          md_file.write(body + '\n')


def convert_to_coderegation_post(filename):
    with open(filename, encoding='utf8') as in_file:
        headers = get_headers(in_file)
        body = get_body(in_file)
    write_output(headers, body)


if __name__ == "__main__":
    convert_to_coderegation_post(SOURCE_FILENAME)
