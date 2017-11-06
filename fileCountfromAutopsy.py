import re
import sqlite3
import os.path
from collections import Counter
import pprint


targetExtensions = [
                    '.doc',
                    '.docx',
                    '.jpg',
                    '.bmp',
                    '.jpeg',
                    '.tif',
                    '.sqlite',
                    '.db',
                    '.zip',
                    '.txt',
                    '.dll',
                    '.exe',
                    '.zip',
                    '.lnk',
                    '.sys',
                    '.png',
                    '.mpg',
                    '.pdf'
                    ]

def pretty_printer(o):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)


path_to_db = r'C:\Users\ric\Dropbox\Uni\CSG5126\Assignment 2\autopsy.db'

extensions = []
with sqlite3.connect(path_to_db) as conn:
    cursor = conn.cursor()

    sql = """
    select name from tsk_files
    where md5 is not null
    """
    cursor.execute(sql)

    for row in cursor.fetchall():
        fileName = row[0]
        _, ext = os.path.splitext(fileName)
        extensions.append(ext.lower())

c = Counter(extensions)

stuff = {}
for item, count in c.items():
    print(item,count,sep="|")
    if item in targetExtensions:
        stuff[item] = count
    else:
        if '_other' not in stuff:
            stuff['_other'] = 0
        stuff['_other'] += count

for item, count in reversed(sorted(stuff.items(), key=lambda x: x[1])):
    print(item[1:], count, sep='|')


        