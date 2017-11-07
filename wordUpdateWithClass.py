# -*- coding: utf-8 -*-

import win32com.client
import re
import pprint
import datetime
import json
import yaml
import time

def pretty_print(o):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)


def split_chunks(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

class Word:

    def __init__(self, path):
        self.path = path
        self.app = win32com.client.gencache.EnsureDispatch('Word.Application')
        self.app.Visible = True
        self.app.DisplayAlerts = False
        self.app.Documents.Open(self.path)
        self.doc = self.app.ActiveDocument
        
    def updateTable(self, bookmark, data, heading_rows=1):
        word_range = self.doc.Bookmarks(bookmark).Range 
        table = word_range.Tables(1)
        rows_count = table.Rows.Count
        if not rows_count >= len(data) + heading_rows:
            table.Select()
            self.app.Selection.InsertRowsBelow(NumRows=len(data) + heading_rows - rows_count)
        i = heading_rows
        for entry in data: #sorted(data, key=lambda x: (x[0], x[1])):
            i += 1
            for n in range(len(entry)):
                table.Cell(i, n+1).Range.Text = entry[n]

    def updateIDs(self, bookmark, prefix):
        rex = re.compile('[A-Z]+', re.IGNORECASE)
        word_range = self.doc.Bookmarks(bookmark).Range 
        table = word_range.Tables(1)
        rows_count = table.Rows.Count
        count = 0
        for rid in range(1, rows_count+1):
            m = rex.search(table.Cell(rid, 1).Range.Text)
            if m:
                pass
            else:
                count+=1
                table.Cell(rid,1).Range.Text = f"{prefix}{str(count).zfill(3)}"


def make_data():
    data = """
File system: NTFS
Total capacity: 17,406,361,600 bytes = 16.2 GB
Sector count: 33,996,800
Bytes per sector: 512
Bytes per cluster: 4,096
Free clusters: 78,466 = 2% free
Total clusters: 4,249,599
NTFS version: 3.1
Volume flags: 0x0000
Volume GUID: {76244106-0D26-4AB8-9B41-2440BD9C35D0}
Serial No.: 32858228 (hex)
Serial No.: 28828532 (hex, rev)
Serial No.: 679642418 (dec, rev)
""".splitlines()
    # data = [x.split(':') for x in data if len(x) > 0]
    with open(r'C:\Users\rdapaz\projects\csg5126_assignment2_scripts\history.json', 'r') as f:
        data =json.load(f)
    new_data = []
    for dttm, event, category in data:
        new_data.append(['', dttm, event, category])
    return new_data

def main(bookmark, data=[], heading_rows=1):
    my_path = r'C:\Users\rdapaz\Dropbox\Uni\CSG5126\Assignment 2\CSG5126 Assignment 2 - Ricardo da Paz_V2.docx'
    wd = Word(my_path)
    # wd.updateTable(bookmark, data, heading_rows)
    # time.sleep(1)
    wd.updateIDs(bookmark, prefix="T")

def mock(data, **kwargs):
    pretty_print(data)
    
if __name__ == "__main__":
    data = make_data()
    # mock(bookmark='bk3', data=data, heading_rows=1)
    main(bookmark='timeline', data=data, heading_rows=1)
    # main(bookmark='Financials1', data=data, heading_rows=1)





