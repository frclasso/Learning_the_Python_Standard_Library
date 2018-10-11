#!/usr/bin/env python3

# HTTP package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224
import urllib.request
import json
import textwrap

with urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224') as f:
    text = f.read()
    decoded_text = text.decode('utf-8')
    print(textwrap.fill(decoded_text, width=70))

print()
obj =json.loads(decoded_text)
print(obj['kind'])

print()
print('TextSnippet')
print(obj['items'][0]['searchInfo']['textSnippet'])