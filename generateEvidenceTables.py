# coding: utf-8

import os
import os.path
import pprint
import win32com.client


def pretty_printer(o):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)


def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

class Word:
    def __init__(self, path):
        self.path = path
        self.app = win32com.client.gencache.EnsureDispatch("Word.Application")
        self.app.Visible = True
        self.app.DisplayAlerts = False
        self.doc = self.app.Documents.Open(self.path)
        self.rge = self.doc.Range(Start=0, End=0)

    def initialise(self):
        self.rge.InsertAfter("\n\n")
        self.rge.Select

    def insert_table(self, autoTextName = 'evt'):
        self.app.Selection.TypeText(Text=autoTextName)
        self.app.Selection.Range.InsertAutoText()
        rge = self.doc.Range()
        rge.Select()
        rge.Collapse(0)
        rge.InsertAfter("\n\n")
        rge.Select()

    def updateTable(self, tbl_id, datarow1, datarow2):
        table = self.doc.Tables(tbl_id)
        fileName, folder, ext, modified, changed, accessed, created, size, hash = datarow1
        table.Cell(2, 2).Range.Text = fileName
        table.Cell(3, 2).Range.Text = folder
        table.Cell(4, 2).Range.Text = ext
        table.Cell(5, 2).Range.Text = ''
        table.Cell(6, 2).Range.Text = hash
        table.Cell(7, 2).Range.Text = accessed
        table.Cell(8, 2).Range.Text = created
        table.Cell(9, 2).Range.Text = modified
        table.Cell(10, 2).Range.Text = changed
        table.Cell(11, 2).Range.Text = ''
        table.Cell(12, 2).Range.Text = size
        table.Cell(13, 2).Range.Text = ''

        fileName, folder, ext, modified, changed, accessed, created, size, hash = datarow2
        table.Cell(2, 5).Range.Text = fileName
        table.Cell(3, 5).Range.Text = folder
        table.Cell(4, 5).Range.Text = ext
        table.Cell(5, 5).Range.Text = ''
        table.Cell(6, 5).Range.Text = hash
        table.Cell(7, 5).Range.Text = accessed
        table.Cell(8, 5).Range.Text = created
        table.Cell(9, 5).Range.Text = modified
        table.Cell(10, 5).Range.Text = changed
        table.Cell(11, 5).Range.Text = ''
        table.Cell(12, 5).Range.Text = size
        table.Cell(13, 5).Range.Text = ''



    def generateEvidence(self, data):
        """ Need to ensure that data has an even size"""
        self.initialise()

        tbl_id = 0
        for data_row1, data_row2 in pairwise(data):
            tbl_id += 1
            self.insert_table(autoTextName='evt1')
            self.updateTable(tbl_id, data_row1, data_row2)

data = """
/img_2017-B.dd/Users/computer/Pictures/101438745-cat-conjunctivitis-causes.jpg|2017-06-12 12:01:49 AWST|2017-06-12 12:01:49 AWST|2017-06-12 12:01:47 AWST|2017-06-12 12:01:47 AWST|2528414|0b057be67f220767dd1075594432e8b8
/img_2017-B.dd/Users/computer/Pictures/1817db9a2a947adc1d1e2ebbdf8dcafd.jpg|2017-06-14 07:40:02 AWST|2017-06-14 07:40:02 AWST|2017-06-14 07:40:01 AWST|2017-06-14 07:40:01 AWST|27029|cfc5a8e8a803645232990aaf2ff49fd7
/img_2017-B.dd/Users/computer/Pictures/cat-black-superstitious-fcs-cat-myths-162286659.jpg|2017-06-14 07:39:03 AWST|2017-06-14 07:39:03 AWST|2017-06-14 07:39:03 AWST|2017-06-14 07:39:02 AWST|114394|7e9be033a955f18f777a87d28f93be3e
/img_2017-B.dd/Users/computer/Pictures/cat2.jpg|2017-06-14 07:42:18 AWST|2017-06-14 07:42:18 AWST|2017-06-14 07:42:17 AWST|2017-06-14 07:42:17 AWST|122791|096254b20f79b6728384a54dbba69ea1
/img_2017-B.dd/Users/computer/Pictures/chaton_232339_w620.jpg|2017-06-12 12:03:01 AWST|2017-06-12 12:03:01 AWST|2017-06-12 12:03:01 AWST|2017-06-12 12:03:01 AWST|54663|3fb617f7a7cc758a998410ad4567c126
/img_2017-B.dd/Users/computer/Pictures/f03b7614dfadbbe4c2e8f88b69d12e04.jpg|2017-06-14 07:41:26 AWST|2017-06-14 07:41:26 AWST|2017-06-14 07:41:25 AWST|2017-06-14 07:41:25 AWST|491095|f03b7614dfadbbe4c2e8f88b69d12e04
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/cache2/entries/4C074A918ACE865639183E88679297964650C2DF|2017-07-27 13:32:44 AWST|2017-07-27 13:32:44 AWST|2017-07-27 13:32:43 AWST|2017-07-27 13:32:43 AWST|15696|da632a0e6a0b6ec1c5066078e74b7c7f
/img_2017-B.dd/Users/computer/AppData/Local/Mozilla/Firefox/Profiles/zij1frw0.default/thumbnails/a5e30fd021851bb6f1637fcadbe8fc67.png|2017-07-27 13:27:59 AWST|2017-07-27 13:27:59 AWST|2017-07-27 13:27:59 AWST|2017-07-27 13:27:59 AWST|105462|670a9ce162208598f3efc09945da8f39
/img_2017-B.dd/Users/computer/Documents/thestuff.zip|2017-06-14 07:00:16 AWST|2017-06-14 07:00:50 AWST|2017-06-14 07:00:15 AWST|2017-06-14 07:00:15 AWST|989778|4364f14ecdd1380e8d60c54b92492baa
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3276.doc|2017-06-14 11:08:28 AWST|2017-06-14 11:09:53 AWST|2017-06-14 11:08:27 AWST|2017-06-14 11:02:22 AWST|17408|121956815de6276ddb5f1978e7431149
/img_2017-B.dd/Users/computer/Desktop/NEWS STORIES/#3840.doc|2017-07-27 14:26:50 AWST|2017-07-27 14:26:50 AWST|2017-07-27 14:26:49 AWST|2017-07-27 14:26:05 AWST|17408|6f36f7cde31efc87d3edeb2d80060591
/img_2017-B.dd/stuff.txt|2017-06-14 07:48:56 AWST|2017-06-14 08:02:23 AWST|2017-06-14 07:48:56 AWST|2017-06-14 07:48:56 AWST|10485760|b436d314e9918621f8341fa4105da41d
/img_2017-B.dd/Users/computer/Desktop/foryou.txt|2017-05-17 16:34:47 AWST|2017-05-17 16:34:47 AWST|2017-05-17 16:34:43 AWST|2017-05-17 16:34:42 AWST|1048576|318175c7f653f2480944c3ed3f61bcca
/img_2017-B.dd/Users/computer/Documents/Links.docx|2017-06-14 08:01:26 AWST|2017-06-14 08:01:26 AWST|2017-06-14 08:01:26 AWST|2017-06-14 08:01:26 AWST|11100|4e0af85db16d3ba53a221363346a3d8e
""".splitlines()

data = [x.split('|') for x in data if len(x) > 0]

new_data = []
""" Todo: check all files against the file command in SIFT"""
for fullName, modified, changed, accessed, created, size, hash in data:
    file = os.path.basename(fullName)
    folder = os.path.dirname(fullName)
    ext = (os.path.splitext(fullName)[1])[1:].upper() #This is cheating but will do manual check later
    new_data.append([file, folder, ext, modified, changed, accessed, created, size, hash])

wordTemplatePath = r'C:\Users\ric\Dropbox\Uni\CSG5126\Assignment 2\CSG5126 Assignment 2 - Presentation of ContentV2.docx'
word = Word(wordTemplatePath)
word.generateEvidence(new_data)
