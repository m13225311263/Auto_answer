#encoding=utf-8
import csv
import sys
import os
class csv2txt:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.data=[]
        self.readDir='data'
        self.saveDir='dataR'
        self.files=os.listdir(self.readDir)
        l=len(self.files)
        print ("number of files:"+str(l))
        for i in xrange(l):
            self.readAndWriteFile(self.files[i])
        #self.data_list = [item.decode('utf-8') for item in self.data]


    def read(self,readname):
        with open(readname, 'rU') as csvfile:
            data_row = csv.reader(csvfile, delimiter=' ')
            for row in data_row:
                temp=[]
                temp.append(row[0]) #BOS
                temp.append(row[1].decode('utf-8')) #question
                temp.append('EOS\t') # loal
                temp.append(row[-1]) #tag
                self.data.append(temp)

    def write(self, data_list):
        writename = self.saveDir + '/' + 'result.csv'
        data=[' '.join(item) for item in data_list]
        fo = open(writename, 'w')
        for sen in data:
            fo.write(sen+'\n')
        print('Finish writing')
        fo.close()


    def readAndWriteFile(self,file):
        name=file[0:-4]
        readname=self.readDir+'/'+file
        writename=self.saveDir+'/'+name+'.txt'
        #read
        self.read(readname)

        #write
        #self.write(writename,data)
        #print("writing files has finished")

    def getDataList(self):
        return self.data

'''
a=csv2txt()
b=a.getDataList()
print b[0]
'''