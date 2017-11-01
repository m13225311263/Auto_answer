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
        l=len(self.files)
        print ("number of topics :"+str(l))
        for i in xrange(l):
            self.readAndWriteFile(self.files[i])
    def read(self,readname,data):
        with open(readname, 'rU') as csvfile:
            data_row = csv.reader(csvfile, delimiter=' ')
            for row in data_row:
                data.append(row[1])
        data_list = [item.decode('utf-8') for item in data]
        return data_list

    def write(self, writename, data_list):
        fo = open(writename, 'w')
        for item in data_list:
            for w in item:
                str = w + ""
                fo.write(str)
        fo.close()


    def readAndWriteFile(self,file):
        data=[]
        name=file[0:-4]
        readname=self.readDir+'/'+file
        writename=self.saveDir+'/'+name+'.txt'
        #read
        data=self.read(readname,data)

        #write
        self.write(writename,data)
        print("writing files has finished")
'''
a=csv2txt()
'''