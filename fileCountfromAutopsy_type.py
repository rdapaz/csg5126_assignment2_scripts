import re
import sqlite3
import os.path
from collections import Counter
import pprint


targetExtensions = [
                    'doc',
                    'docx',
                    'jpg',
                    'bmp',
                    'jpeg',
                    'tif',
                    'sqlite',
                    'db',
                    'zip',
                    'txt',
                    'dll',
                    'exe',
                    'zip',
                    'lnk',
                    'sys',
                    'png',
                    'mpg',
                    'pdf'
                    ]

def pretty_printer(o):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)


path_to_db = r'C:\Users\rdapaz\Dropbox\Uni\CSG5126\Assignment 2\autopsy.db'

extensions = {}
with sqlite3.connect(path_to_db) as conn:
    cursor = conn.cursor()

    sql = """
    SELECT extension, count(t.extension) from tsk_files t 
    where t.md5 is not null group by 1 order by 2 desc
    """
    cursor.execute(sql)

    for row in cursor.fetchall():
        ext, count = row
        extensions[ext] = count

stuff = {}
for item, count in extensions.items():
    if item in targetExtensions or count > 5000:
        stuff[item] = count
    else:
        if 'other' not in stuff:
            stuff['other'] = 0
        stuff['other'] += count

for item, count in reversed(sorted(stuff.items(), key=lambda x: x[1])):
    print(item, count, sep='|')