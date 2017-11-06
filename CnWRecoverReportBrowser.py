import win32com.client
import re
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


target_extensions = [
                    '.jpg',
                    '._j_p_g_',
                    '.zip',
                    '.txt',
                    '.png',
                    '.pdf',
                    ]

class Excel:

    def __init__(self, path, sheet):
        self.path = path
        self.shetName = sheet
        self.xlApp = win32com.client.gencache.EnsureDispatch('Excel.Application')
        self.xlApp.Visible = True
        self.wk = self.xlApp.Workbooks.Open(self.path)
        self.sh = self.wk.Worksheets(self.shetName)

    def getListofFiles(self):
        self.files = []
        eof = self.sh.Range('A65536').End(-4162).Row
        for row in range(2, eof+1):
            file = self.sh.Range(f'D{row}').Value if self.sh.Range(f'D{row}').Value else None
            if file:
                _, file_extension = os.path.splitext(file)
                if file_extension in target_extensions:
                    self.files.append(file)
        return self.files

    def updateHash(self, hash):
        eof = self.sh.Range('A65536').End(-4162).Row
        for row in range(2, eof+1):
            fullFilePath = self.sh.Range(f'D{row}').Value if self.sh.Range(f'D{row}').Value else None
            if fullFilePath:
                file = os.path.basename(fullFilePath)
                if file in hash:
                    self.sh.Range(f'Z{row}').Value = hash[file]
        


path = r'C:\Users\ric\ownCloud\Uni\CnWRecover_Report.xlsx'
sheet = 'files_13'
xl = Excel(path=path, sheet=sheet)
files = xl.getListofFiles()

filesnHashes = {}
for file in files:
    try:
        md5Hash = md5(file)
        print(os.path.basename(file), md5Hash, sep="|")
        filesnHashes[os.path.basename(file)] = md5Hash
    except:
        pass

xl.updateHash(filesnHashes)