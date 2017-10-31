import numpy as np
import csv
import jieba

class dataPreproce:
    def __init__(self,fileName='./data/data.csv'):
        self.fn=fileName
        self.data=[] #(question list)
        self.num_lable=[] #(questionNumber,lable)
        with open(self.fn,'rU') as csvfile: #用excel转换的用 rU
            data_row=csv.reader(csvfile,delimiter=' ')
            for row in data_row:
                self.data.append(row[1])
                lableitem=(row[0][0:1],row[-1])
                self.num_lable.append(lableitem)


    #分割单个的字
    def wordsplit(self,data):
        list=[]
        for i in data:
            item=[a for a in i]
            list.append(item)
        return list


    #word2Vector转向量

    #对句子进行填充
    def padding_data(self,data):
        data=[item.decode('utf-8') for item in data]
        max_len=max([len(s) for s in data])
        row=len(data)
        sentens


    def getdata(self):
        return self.data

    def getLable(self):
        return self.num_lable



a=dataPreproce()
data=a.getdata()
label=a.getLable()
print(len(label),len(data[0]))