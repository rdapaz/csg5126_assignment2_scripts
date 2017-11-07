# -*- coding: utf-8 -*-
import re
import yaml
import pprint
import datetime
import os


def pretty_printer(o):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)


with open(r'C:\Users\rdapaz\ownCloud\Uni\RegRipper\UAFiles.yaml', 'r') as yaml_file:
    data = yaml.load(yaml_file)

execs = []

#{9E3995AB-1F9C-4F13-B827-48B24B6C7174}\TaskBar\File Explorer.lnk (34)
rex = re.compile(r'(.*)\s\((.*)\)')
for dt, exec_list in data.items():
    dt = datetime.datetime.strptime(dt, '%a %b %d %H:%M:%S %Y Z')
    dt2 = dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
    for entry in exec_list:
        m = rex.search(entry)
        if m:
            fullname = m.group(1)
            count = m.group(2)
            file = os.path.basename(fullname)
            execs.append([dt2, file, count])

execs = list(reversed(sorted(execs, key=lambda x: x[0])))

for dt, exec, count in execs:
    print(dt, exec, count, sep="|")
