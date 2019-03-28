#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import requests
import shutil

# check the number of parameters
if len(sys.argv) != 3:
    print('Usage: python curl-mdc.py <URL> <OUTPUT_DIR>')
    print('       You need to enter a URL that contains a file name')
    print('       Examples -> URL:https://tera-net.com/dl/tpad/tpad109.zip  OUTPUT_DIR:/tmp')
    sys.exit(1)

url = sys.argv[1]
output_dir = sys.argv[2]
filename = os.path.basename(url)

if filename is None:
    print('ERROR: You need to enter a URL that contains a file name')
    exit(1)

try:
    res = requests.get(url, stream=True)
    print(res.status_code)
    if res.status_code == 200:
        with open(output_dir + '/' + filename, 'wb') as file:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, file)
except requests.exceptions.RequestException as err:
    print(err)

