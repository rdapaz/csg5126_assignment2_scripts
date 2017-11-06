#!/usr/bin/python3
'''
This script is used to characterise the output from running
the sorter command against a drive image, where the 
output is saved in /home/sansforensics/Desktop/save_dir.

It outputs the filename, the number of entries and the number
of mismatched entries where the file extension does not match the
output from running a file command in Linux
'''
from collections import Counter
import re
import os
import hashlib
import pprint


def pretty_printer(o):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def countEntries(text_data):
    entry_count = 0
    mismatch_count = 0
    for line in text_data.splitlines():
        if line.startswith(r'C:/'):
            entry_count += 1
        elif 'Extension Mismatch!' in line:
            mismatch_count += 1
    return (entry_count, mismatch_count)


def countExtensions(text_data):
    file_ext = []
    rex = re.compile(r'(C\:.*)\n'
                 r'.*\n'
                 r'(?:\s+--- Extension Mismatch! ---\n)?'
                 r'(?:\s+Image\:.*\s+Inode\:\s+(\d+)\-\d+\-\d+)', 
                 re.MULTILINE | re.VERBOSE)
    ext_rex = re.compile(   r'(.*)'
                            r'\.'
                            r'([a-z])\Z',
                        (re.IGNORECASE | re.VERBOSE))
    for file_path, _ in rex.findall(text_data):
        try:
            filename, ext = os.path.splitext(file_path)
        except:
            ext = 'none'
        ext = ext[1:]
        file_ext.append(ext.lower())

    c = Counter(file_ext)
    arr = []
    for k, v in reversed(sorted(c.items(), key=lambda x: x[1])):
        arr.append("{}: {}".format(k, v))
    return ", ".join(arr)


rex = re.compile(r'.*\.txt')

filesNhashes = {}
for root, dirs, files in os.walk(r'/home/sansforensics/Desktop/save_dir'):
    print(root)
    for file in files:
        m = rex.search(file)
        if m:
            hash_value = md5(os.path.join(root, file))
            with open(os.path.join(root, file), 'r') as fin:
                data = fin.read()
                filesNhashes[file] = dict(md5=hash_value, 
                                                count=countEntries(data)[0], 
                                                mismatch=countEntries(data)[1],
                                                exts = countExtensions(data)
                                            )

            print(file, hash_value, filesNhashes[file]['count'], 
                    filesNhashes[file]['mismatch'],  sep="|")

pretty_printer(filesNhashes)
