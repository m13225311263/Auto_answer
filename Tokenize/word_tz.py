#encoding=utf-8
import sys
import jieba
jieba.load_userdict("dict.txt")
import jieba.posseg as pseg
import codecs
from readAndWrite import csv2txt

class word_tokenizater:
    def __init__(self,data):
        reload(sys)
        sys.setdefaultencoding('utf8')
        stop_words = 'stopwords.txt'
        self.data=data
        self.result=[]
        self.stopwords = codecs.open(stop_words, 'r', encoding='utf8').readlines()
        self.stopwords = [w.strip() for w in self.stopwords]
        # [标点符号、连词、助词、副词、介词、时语素 p：、‘的’、数词:m、方位词、代词]
        self.stop_flag = ['x', 'c', 'u', 'd', 'uj', 'f', 'r']

    # file tokenization
    def tokenization(self):
        for sentence in self.data:
            result=[]
            words=pseg.cut(sentence[1])
            #remove stop words
            for word, flag in words:
                if flag not in self.stop_flag and word not in self.stopwords :
                    result.append(word)
            o=[sentence[2]]
            for i in range(len(result)):
                o.append('O ')
            o.append('O')
            sentence[1]=" ".join(result)
            sentence[2]="".join(o)
        return self.data
'''
#get data
read_data=csv2txt()
data=read_data.getDataList()
print data[0][1]
    #token
tk=word_tokenizater(data)
data=tk.tokenization()
print data[0]
'''