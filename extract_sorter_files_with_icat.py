#!/usr/bin/python3
'''
This script uses the output from the analyse_files.py script
to identify and run the icat command to recover a whole
bunch of significant files by name for analysis 
'''
import re
import os
import os.path
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


data = '''
doc|#3840.doc
doc|#3295.doc
html|register.html
doc|#3276.doc
doc|#3250.doc
docx|#3276.docx
txt|foryou.txt
txt|stuff.txt
docx|Links.docx
jpg|Siamese-Cat-Names.jpg
jpg|adopting-a-cat.jpg
jpg|4426323.jpg
jpg|cat2.jpg
jpg|f03b7614dfadbbe4c2e8f88b69d12e04.jpg
jpg|cute-kitten-catcute-little-cat-hd-for-desktop-of-cute-white-kitten.jpg
jpg|HP_PCC_md_0130_cat53.jpg
jpg|1817db9a2a947adc1d1e2ebbdf8dcafd.jpg
jpg|czarny-kot-fakt.jpg
jpg|cat-black-superstitious-fcs-cat-myths-162286659.jpg
zip|thestuff.zip
jpg|cat-03.jpg
jpg|cat-adult-landing-hero.jpg
jpg|chaton_232339_w620.jpg
jpg|4-ways-cheer-up-depressed-cat.jpg
jpg|101438745-cat-conjunctivitis-causes.jpg
jpg|3385141-cat-images.jpg
jpg|7dd84d70-768b-492b-88f7-a6c70f2db2e9.jpg
jpg|e0194eca1c8135636ce0e014341548c3.jpg
jpg|cutest-cat-picture-ever.jpg
jpg|cute-cat.jpg
txt|enjoy.txt
pdf|superman.pdf
docx|#3250.docx
txt|text.txt
docx|#3249.docx
docx|#3247.docx
'''.splitlines()

target_files = [x.split('|')[1] for x in data if len(x) > 0]

rex = re.compile(r'(C\:.*)\n'
                 r'.*\n'
                 r'(?:\s+--- Extension Mismatch! ---\n)?'
                 r'(?:\s+Image\:.*\s+Inode\:\s+(\d+)\-\d+\-\d+)', 
                 re.MULTILINE | re.VERBOSE)

rex_filetypes = re.compile(r'\.txt')
for root, dirs, files in os.walk(r'/home/sansforensics/Desktop/save_dir'):
    for file in files:
        m = rex_filetypes.search(file)
        if m:
            with open(os.path.join(root, file), 'r') as fin:
                data = fin.read()

            for full_name, inode in rex.findall(data):
                filename = os.path.basename(full_name)
                if filename in target_files:
                    print('[+] processed {}'.format(filename))
                    try:
                        folder = r'/media/sansforensics/Forensics/uni/CSG5126/Assignment2/Image'
                        cmd = 'icat {}/2017-B.dd {} > {}/recovery/{}'.format(folder, inode, folder, filename)
                        os.system(cmd) 
                    except:
                        pass

for root, dirs, files in os.walk(r'/media/sansforensics/Forensics/uni/CSG5126/Assignment2/Image/recovery'):
    for file in files:
        hash_value = md5(os.path.join(root, file))
        filename = os.path.basename(file)
        print(filename, hash_value, sep="|")