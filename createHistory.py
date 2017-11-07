
import pprint
import os.path
import datetime
import yaml
import sqlite3
import json

def pretty_printer(o):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)

history = []


data = """
/img_2017-B.dd/Users/computer/Pictures/101438745-cat-conjunctivitis-causes.jpg|2017-06-12 12:01:49 AWST|2017-06-12 12:01:47 AWST
/img_2017-B.dd/Users/computer/Pictures/1817db9a2a947adc1d1e2ebbdf8dcafd.jpg|2017-06-14 07:40:02 AWST|2017-06-14 07:40:01 AWST
/img_2017-B.dd/Users/computer/Pictures/cat-black-superstitious-fcs-cat-myths-162286659.jpg|2017-06-14 07:39:03 AWST|2017-06-14 07:39:02 AWST
/img_2017-B.dd/Users/computer/Pictures/cat2.jpg|2017-06-14 07:42:18 AWST|2017-06-14 07:42:17 AWST
/img_2017-B.dd/Users/computer/Pictures/chaton_232339_w620.jpg|2017-06-12 12:03:01 AWST|2017-06-12 12:03:01 AWST
/img_2017-B.dd/Users/computer/Desktop/encrypted|2017-05-23 06:20:01 AWST|2017-05-23 06:20:00 AWST
/img_2017-B.dd/Users/computer/Desktop/foryou.txt|2017-05-17 16:34:47 AWST|2017-05-17 16:34:42 AWST
/img_2017-B.dd/Users/computer/Documents/thestuff.zip|2017-06-14 07:00:16 AWST|2017-06-14 07:00:15 AWST
/img_2017-B.dd/Users/computer/Pictures/f03b7614dfadbbe4c2e8f88b69d12e04.jpg|2017-06-14 07:41:26 AWST|2017-06-14 07:41:25 AWST
/img_2017-B.dd/Users/computer/Downloads/TrueCrypt/TrueCrypt User Guide.pdf|2017-05-17 16:40:51 AWST|2017-05-17 16:40:51 AWST
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/4C074A918ACE865639183E88679297964650C2DF|2017-07-27 13:32:44 AWST|2017-07-27 13:32:43 AWST
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/thumbnails/a5e30fd021851bb6f1637fcadbe8fc67.png|2017-07-27 13:27:59 AWST|2017-07-27 13:27:59 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3247.docx|2017-05-17 11:32:49 AWST|2017-05-17 11:32:48 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3249.docx|2017-05-17 11:34:56 AWST|2017-05-17 11:34:56 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3250.docx|2017-05-17 11:45:21 AWST|2017-05-17 11:45:21 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3276.doc|2017-06-14 11:08:28 AWST|2017-06-14 11:02:22 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3295.doc|2017-06-21 09:05:56 AWST|2017-06-21 09:05:55 AWST
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3840.doc|2017-07-27 14:26:50 AWST|2017-07-27 14:26:05 AWST
/img_2017-B.dd/stuff.txt|2017-06-14 07:48:56 AWST|2017-06-14 07:48:56 AWST
/img_2017-B.dd/Users/computer/Desktop/foryou.txt|2017-05-17 16:34:47 AWST|2017-05-17 16:34:42 AWST
/img_2017-B.dd/Users/computer/Documents/Links.docx|2017-06-14 08:01:26 AWST|2017-06-14 08:01:26 AWST
""".splitlines()

data = [x.split('|') for x in data if len(x) > 0]
'''
for fullpath, modified, _ in data:
    file = os.path.basename(fullpath)
    modified = modified[:16]
    modified = datetime.datetime.strptime(modified, '%Y-%m-%d %H:%M')
    event = f'Modified file {file}'
    history.append([modified, event])
'''
for fullpath, _, created in data:
    file = os.path.basename(fullpath)
    created = created[:16]
    created = datetime.datetime.strptime(created, '%Y-%m-%d %H:%M')
    event = f'Created file {file}'
    history.append([created, event])

path_to_db = r'places.sqlite'

TIMEBAND = 60 # in hours

augmented_history = []
with sqlite3.connect(path_to_db) as conn:
    cursor = conn.cursor()

    for dttm, event in history:
        augmented_history.append([dttm.strftime('%Y-%m-%d %H:%M'), event, 'File creation event'])
        
        dttm1 = dttm - datetime.timedelta(minutes=TIMEBAND)
        dttm2 = dttm + datetime.timedelta(minutes=TIMEBAND)

        sql = """
            SELECT dt, url, title, url_hash FROM (
            SELECT moz_places.id, 
            datetime (visit_date/1000000,'unixepoch','localtime') AS visit_date, 
            strftime('%Y-%m-%d %H:%M',datetime (visit_date/1000000,'unixepoch','localtime')) AS dt,
            url, title,visit_count,typed,hidden,frecency, url_hash FROM moz_places, moz_historyvisits 
            WHERE moz_places.id=moz_historyvisits.place_id 
            AND (url LIKE '%cat%' OR url LIKE '%youtube%') AND (dt BETWEEN ? AND ?) LIMIT 5)
            """
        cursor.execute(sql, [dttm1.strftime('%Y-%m-%d %H:%M'), dttm2.strftime('%Y-%m-%d %H:%M')])

        for row in cursor.fetchall():
            dt, url, title, url_hash = row
            if len(augmented_history) > 0:
                if url_hash not in [x[2] for x in augmented_history]:
                    augmented_history.append([dt, f'{title}\n{url}', url_hash])
            else:
                augmented_history.append([dt, f'{title}\n{url}', url_hash])


with open(r'email_exchanges.yaml', 'r') as fin:
    email_timeline = yaml.load(fin)

email_timeline = [[datetime.datetime.strptime(x, '%d/%m/%Y %H:%M'), y] for x, y in email_timeline.items()]

for dttm, email_info in email_timeline:
    augmented_history.append([dttm.strftime('%Y-%m-%d %H:%M'), email_info, 'Email interaction event'])



# '''
#Here we use the information that we already had developed from our analysis
#of UserAssist

more_data = """
2017-06-14 07:57:10+08:00|Launched WPS Writer
2017-06-14 07:50:06+08:00|Launched TrueCrypt
2017-06-14 07:43:31+08:00|Formatted a drive with TrueCrypt
2017-06-12 11:51:31+08:00|Launched Mozilla Thunderbird
2017-05-31 06:36:26+08:00|Launched MSPaint
2017-05-19 03:50:45+08:00|Launched Mozilla Thunderbird from a link
2017-05-17 16:40:32+08:00|Set up TrueCrypt
2017-05-17 11:39:53+08:00|Launched WPS Writer from the command line
2017-05-17 11:39:27+08:00|Launched Kingsoft /WPS Writer
2017-05-17 09:42:17+08:00|Installed Thunderbird
2017-05-17 09:31:05+08:00|Installed Firefox
2017-05-09 08:08:04+08:00|Launched MSPaint from link
2017-05-09 08:08:04+08:00|Lauched Snipping Tool link
""".splitlines()

more_data = [x.split('|') for x in more_data if len(x) > 0]

for dttm, event in more_data:
    dttm = dttm[:16]
    dttm = datetime.datetime.strptime(dttm, '%Y-%m-%d %H:%M')
    augmented_history.append([dttm.strftime('%Y-%m-%d %H:%M'), event, 'Application install/run event'])
# '''
augmented_history =sorted(augmented_history, key=lambda x: x[0])
pretty_printer(augmented_history)
print(len(augmented_history))

with open(r'C:\Users\rdapaz\projects\csg5126_assignment2_scripts\history.json', 'w') as fout:
    json.dump(augmented_history, fout, indent=True)