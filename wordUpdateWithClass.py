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
manifest|41887|0|0%
png|20675|1|0%
dll|19793|0|0%
cat|12795|0|0%
mui|9648|0|0%
mum|7623|0|0%
no extension|7349|36|0%
exe|2856|0|0%
sys|1415|0|0%
jpg|1029|37|4%
lnk|362|0|0%
txt|361|3|1%
bmp|298|0|0%
db|80|0|0%
mpg|53|0|0%
doc|40|3|8%
sqlite|28|0|0%
zip|5|2|40%
docx|4|4|100%
tif|2|0|0%
pdf|1|1|100%
""".splitlines()
    """
    .splitlines()

        return data
    """
    data = [x.split('|') for x in data if len(x) > 0]
    # with open(r'C:\Users\ric\Desktop\Protect the Network - Closeout Report\lessons.json', 'r') as f:
        # data =json.load(f)
    # new_data = []
    # for k, v in data.items():
    #     new_data.append([k, v])
    # new_data = [x.split('|') for x in data if len(x) > 0]
    return data

def main(bookmark, data=[], heading_rows=1):
    my_path = r'C:\Users\ric\Dropbox\Uni\CSG5126\Assignment 2\CSG5126 Assignment 2 - Ricardo da Paz (P).docx'
    wd = Word(my_path)
    wd.updateTable(bookmark, data, heading_rows)
    # time.sleep(1)
    # wd.updateIDs(bookmark, prefix="LES_")

def mock(data, **kwargs):
    pretty_print(data)
    
if __name__ == "__main__":
    data = make_data()
    # mock(bookmark='bk3', data=data, heading_rows=1)
    main(bookmark='bk2', data=data, heading_rows=1)
    # main(bookmark='Financials1', data=data, heading_rows=1)





