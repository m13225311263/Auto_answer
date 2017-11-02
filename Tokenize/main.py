#encoding=utf-8
from readAndWrite import  csv2txt
from word_tz import word_tokenizater

if __name__=="__main__":
    #get data
    oi_data=csv2txt()
    origin_data=oi_data.getDataList()
    #token
    tk=word_tokenizater(origin_data)
    tk_data=tk.tokenization()
    print tk_data[0]
    #write
    oi_data.write(tk_data)



