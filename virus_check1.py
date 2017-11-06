#!/usr/bin/python3
'''
This gets all inodes associated with one of the sorter folders so that we can
extract the files...
'''
import re
import subprocess
import os
import os.path

api='c54357bc51ad74f136441de19c093c1da7fe66c47f2a77cfd706e26b6385c88c'
print(api)

rex = re.compile(r'(C\:.*)\n'
                 r'.*\n'
                 r'(?:\s+--- Extension Mismatch! ---\n)?'
                 r'(?:\s+Image\:.*\s+Inode\:\s+(\d+)\-\d+\-\d+)', 
                 re.MULTILINE | re.VERBOSE)

with open(r'/home/sansforensics/Desktop/save_dir/exec.txt', 'r') as fin:
    data = fin.read()

#icat 2017-B.dd 0 > mft.raw

count = 0
for folder, inode in rex.findall(data):
    filename = os.path.basename(folder)
    with open(r'/home/sansforensics/Desktop/img/params.txt', 'a') as fout:
        fout.write('{}|{}\n'.format(filename, inode))
    try:
        folder = r'/media/sansforensics/Forensics/uni/CSG5126/Assignment2/Image'
        cmd = 'icat {}/2017-B.dd {} > {}/execs/{}'.format(folder, inode, folder, filename)
        os.system(cmd) 
    except:
        pass

