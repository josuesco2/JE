#!/usr/bin/env python

import os
from prettytable import PrettyTable

RESOURCE = '/etc/services'

'CHECK IF THE FILE EXIST'
def exist(obj):
    return True if os.path.isfile(obj) else False

'LETS BUILD A PRETTY TABLE'

table = PrettyTable(['PORT-NAME', 'PORT'])
table.align['PORT-NAME'] = 'l'
table.padding_with = 1

if exist(RESOURCE):
    with open(RESOURCE, 'r') as input:
        for line in input:
            line = line.strip()
            parse = line.split()
            try:
                if parse[0] == '#':
                    continue
                table.add_row([parse[0], parse[1]])
            except IndexError:
                continue

print table





