#encoding=utf-8
from readAndWrite import  csv2txt
from word_tz import word_tokenizater

if __name__=="__main__":
    #get data
    read_data=csv2txt()
    data=read_data.getDataList()
    #token
    tk=word_tokenizater(data)
    data=tk.tokenization(data)



