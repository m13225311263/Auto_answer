import numpy as np
import csv
import jieba
import sys


class dataPreproce:
    def __init__(self,fileName='./data/data.csv'):
        reload(sys)
        sys.setdefaultencoding('utf8')
        self.fn=fileName
        self.data=[] #(question list)
        self.num_lable=[] #(questionNumber,lable)
        with open(self.fn,'rU') as csvfile:
            data_row=csv.reader(csvfile,delimiter=' ')
            for row in data_row:
                self.data.append(row[1])
                lableitem=(row[0][0:1],row[-1])
                self.num_lable.append(lableitem)
        data = [item.decode('utf-8') for item in self.data]
        #word takenoze
        self.data=self.word_tokenize(data)
        #word write in txt
        self.writedown(self.data,'vector_train.txt')




    def word_tokenize(self,data):
        sentence_n=[]
        for sentence in data:
            result=jieba.tokenize(sentence,mode="default")
            result_s=[tk[0] for tk in result]
            sentence_n.append(result_s)
        return sentence_n


    #word2vec
    '''
    def padding_data(self,data):
        
        max_len=max([len(s) for s in data])
        row=len(data)
        sentence
    '''

    def getdata(self):
        return self.data

    def getLable(self):
        return self.num_lable

    def writedown(self,data,name):
        fo=open(name,'w')
        for item in data:
            for w in item:
                str=w+" "
                fo.write(str)
        fo.close()




a=dataPreproce()
data=a.getdata()
print(data[0][0])
label=a.getLable()
