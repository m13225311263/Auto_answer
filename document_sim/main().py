from doc_Similarity import doc_Similarity
from csv2txt import  csv2txt


def writeTotxt(writename,data_list):
    fo = open(writename, 'w')
    fo.write('queryID,topicId,similarity'+'\n')
    for item in data_list:
        s = ''.join([str(j)+',' for j in item])
        fo.write(s+"\n")
    fo.close()


if __name__=="__main__":
    # change the csv file to txt and store it in folder data (dataOrg store origin data csv)
    changeCSV2Txt = csv2txt()

    # get similarity_mat
    model = doc_Similarity()
    similarity_mat = model.getResultMat()
    writeTotxt('result_mat.txt',similarity_mat)



