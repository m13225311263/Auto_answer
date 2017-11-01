#encoding=utf-8
import sys
import jieba.posseg as pseg
import codecs
import os
from gensim import corpora, models, similarities

class doc_Similarity:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf8')
        stop_words = 'stopwords.txt'
        self.result=[]
        self.stopwords = codecs.open(stop_words, 'r', encoding='utf8').readlines()
        self.stopwords = [w.strip() for w in self.stopwords]
        # [标点符号、连词、助词、副词、介词、时语素、‘的’、数词、方位词、代词]
        self.stop_flag = ['x', 'c', 'u', 'd', 'p', 't', 'uj', 'm', 'f', 'r']
        self.dirName='data'
        self.topicNum=0

        #deal with file and calculate similiraty between each two topics
        self.result=self.dealWithfiles()

    # file tokenization
    def tokenization(self,filename):
        result = []
        name=self.dirName+'/'+filename
        with open(name, 'r') as f:
            text = f.read()
            words = pseg.cut(text)
        for word, flag in words:
            if flag not in self.stop_flag and word not in self.stopwords:
                result.append(word)
        return result

    #read file from dir and tokenizate them
    def dealWithfiles(self):
        files = os.listdir(self.dirName)
        self.topicNum=len(files)
        corpus=[self.tokenization(file) for file in files]

        #establish BOW
        dictionary = corpora.Dictionary(corpus)
        print dictionary
        doc_vectors = [dictionary.doc2bow(text) for text in corpus]
        print ("Establish BOW" )

        #establish TF-idf model for every docs
        tfidf = models.TfidfModel(doc_vectors)
        tfidf_vectors = tfidf[doc_vectors]
        print("Establish TF-IDF model")

    # Establish LSI Model
        lsi=models.LsiModel(tfidf_vectors,id2word=dictionary,num_topics=self.topicNum)
        lsi_vector = lsi[tfidf_vectors]
        index = similarities.MatrixSimilarity(lsi_vector)
        simi_list=[]
        for num in xrange(self.topicNum):
            name=str(num) +'.txt'
            query = self.tokenization(name)
            query_bow = dictionary.doc2bow(query)
            query_lsi = lsi[query_bow]
            sims = index[query_lsi]
            i=0
            for i in xrange(num+1,len(sims)):
                coup=(num,i,sims[i])
                simi_list.append(coup)
        simi_list.sort(key=lambda x:(x[2]),reverse=True)
        return simi_list


    def getResultMat(self):
        return self.result
'''
a=doc_Similarity()
b=a.getResultMat()
print(b)
'''







