#encoding=utf-8
import csv
import sys
import os
class csv2txt:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.readDir='dataOrg'
        self.saveDir='data'
        self.files=os.listdir(self.readDir)
        for file in self.files:
            self.readAndWriteFile(file)

    def readAndWriteFile(self,file):
        data=[]
        name=file[0:1]
        readname=self.readDir+'/'+file
        writename=self.saveDir+'/'+name+'.txt'
        #read
        with open(readname, 'rU') as csvfile:
            data_row = csv.reader(csvfile, delimiter=' ')
            for row in data_row:
                data.append(row[1])
        data_list = [item.decode('utf-8') for item in data]

        #write
        fo = open(writename, 'w')
        for item in data_list:
            for w in item:
                str = w + ""
                fo.write(str)
        fo.close()
'''
a=csv2txt()
'''