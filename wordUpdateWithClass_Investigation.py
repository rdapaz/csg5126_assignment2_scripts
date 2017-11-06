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
    with open(r'C:\Users\ric\ownCloud\Uni\CSG5226_CaseFileTimeline.yaml', 'r') as f:
        data = yaml.load(f)

    new_data = []
    for dttm, rest in data.items():
        dt = datetime.datetime.strptime(dttm, '%d/%m/%Y %H:%M')
        dt_s = datetime.datetime.strftime(dt, '%Y-%m-%d %H:%M')
        aim, method, results = '', '', ''
        for k, v in rest.items():
            if k == 'Aim':
                aim = rest[k].strip()
            elif k == 'Method':
                method = rest[k].strip()
            elif k == 'Results':
                results = rest[k].strip()
        new_data.append(['', dt_s, aim, method, results, '', dt])

    new_data = sorted(new_data, key=lambda x: x[-1])
    new_data = [x[:-1] for x in new_data]

    return new_data

def main(bookmark, data=[], heading_rows=1):
    my_path = r'C:\Users\ric\Dropbox\Uni\CSG5126\Assignment 2\CSG5126 Assignment 2 - Presentation of Content.docx'
    wd = Word(my_path)
    wd.updateTable(bookmark, data, heading_rows)
    time.sleep(1)
    wd.updateIDs(bookmark, prefix="")

def mock(data, **kwargs):
    pretty_print(data)
    
if __name__ == "__main__":
    data = make_data()
    mock(bookmark='bk3', data=data, heading_rows=1)
    main(bookmark='runningsheet', data=data, heading_rows=1)
    # main(bookmark='Financials1', data=data, heading_rows=1)





