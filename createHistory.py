import re
import pprint
import os.path
from datetime import datetime, timedelta

def pretty_printer(o):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)


data = """
/img_2017-B.dd/Users/computer/Desktop/encrypted|2017-05-23 06:20:01 AWST|2017-05-23 06:20:00 AWST
/img_2017-B.dd/Users/computer/Desktop/foryou.txt|2017-05-17 16:34:47 AWST|2017-05-17 16:34:42 AWST
/img_2017-B.dd/Users/computer/Documents/thestuff.zip|2017-06-14 07:00:16 AWST|2017-06-14 07:00:15 AWST
/img_2017-B.dd/Users/computer/Downloads/TrueCrypt/TrueCrypt User Guide.pdf|2017-05-17 16:40:51 AWST|2017-05-17 16:40:51 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3247.docx|2017-05-17 11:32:49 AWST|2017-05-17 11:32:48 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3249.docx|2017-05-17 11:34:56 AWST|2017-05-17 11:34:56 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3250.docx|2017-05-17 11:45:21 AWST|2017-05-17 11:45:21 AWST
/img_2017-B.dd/Users/computer/Documents/thestuff.zip|2017-06-14 07:00:16 AWST|2017-06-14 07:00:15 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3276.doc|2017-06-14 11:08:28 AWST|2017-06-14 11:02:22 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3295.doc|2017-06-21 09:05:56 AWST|2017-06-21 09:05:55 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3840.doc|2017-07-27 14:26:50 AWST|2017-07-27 14:26:05 AWST
/img_2017-B.dd/stuff.txt|2017-06-14 07:48:56 AWST|2017-06-14 07:48:56 AWST
/img_2017-B.dd/Users/computer/Desktop/foryou.txt|2017-05-17 16:34:47 AWST|2017-05-17 16:34:42 AWST
/img_2017-B.dd/Users/computer/Documents/Links.docx|2017-06-14 08:01:26 AWST|2017-06-14 08:01:26 AWST
""".splitlines()

data = [x.split('|') for x in data if len(x) > 0]

history = []
for fullpath, modified, _ in data:
    file = os.path.basename(fullpath)
    modified = modified[:16]
    modified = datetime.strptime(modified, '%Y-%m-%d %H:%M')
    event = f'Modified file {file}'
    history.append([modified, event])

for fullpath, _, created in data:
    file = os.path.basename(fullpath)
    created = created[:16]
    created = datetime.strptime(created, '%Y-%m-%d %H:%M')
    event = f'Created file {file}'
    history.append([created, event])

#Here we use the information that we already had developed from our analysis
#of UserAssist

more_data = """
2017-06-14 07:57:10+08:00|Last launched WPS Writer
2017-06-14 07:50:06+08:00|Last launched TrueCrypt
2017-06-14 07:43:31+08:00|Last formatted a drive with TrueCrypt
2017-06-12 11:51:31+08:00|Last launched Mozilla Thunderbird
2017-05-31 06:36:26+08:00|Last launched MSPaint
2017-05-23 06:18:03+08:00|Last modified UAC Settings
2017-05-19 03:50:45+08:00|Last launched Mozille from a linkMozilla Thunderbird.lnk
2017-05-17 16:40:32+08:00|First set up TrueCrypt
2017-05-17 11:39:53+08:00|Last launched WPS Writer from the command line
2017-05-17 11:39:27+08:00|Last launched Kingsoft /WPS Writer
2017-05-17 09:42:17+08:00|First installed Thunderbird
2017-05-17 09:31:05+08:00|First installed Firefox
2017-05-09 08:08:04+08:00|Last launched MSPaint from link
2017-05-09 08:08:04+08:00|Last lauched Snipping Tool link
""".splitlines()

more_data = [x.split('|') for x in more_data if len(x) > 0]

for dttm, event in more_data:
    dttm = dttm[:16]
    dttm = datetime.strptime(dttm, '%Y-%m-%d %H:%M')
    history.append([dttm, event])

pretty_printer(history)