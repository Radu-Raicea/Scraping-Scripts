# -*- coding: utf-8 -*-
"""Finds the number of modules in the Python Standard Library and exports them to a CSV."""

import csv

import requests
from bs4 import BeautifulSoup

modules = []

html = requests.get('https://docs.python.org/3/py-modindex.html').text

soup = BeautifulSoup(html, 'html.parser')

module_rows = soup.find('table', class_='indextable modindextable').find_all('tr', class_=None)

for module_row in module_rows:
    modules.append([
        module_row.find('code', class_='xref').text,
        module_row.find('em').text
    ])

print(f'Number of modules: {len(modules)}')

with open('modules.csv', 'w') as f:
    writer = csv.writer(f)
    for module in modules:
        writer.writerow(module)

print('Modules written to CSV.')
