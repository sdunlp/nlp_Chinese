# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from snownlp import normal
from snownlp import seg
from snownlp.summary import textrank
from snownlp import SnowNLP
import sys
import os
import os.path
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

if __name__ == '__main__':
# def slp(filename):
    fold=str(sys.argv[1])
    filename="news_test.txt"
    count=0
    cotent=u''
    title=''
    time=''
    abstract=''

    for parent,dirnames,filenames in os.walk("/Users/idejie/Desktop/snownlp/news"):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for dirname in  dirnames:                       #输出文件夹信息
            # print ("parent is:" + parent)
            print  ("dirname is" + dirname)
    #========================================
    #    读取文件的时间、标题、内容ews
    #========================================
    for line in open(fold+filename,'r'):
        if(count==0):
            title=line.replace("标题:","",1)
            count+=1
            # print (title)
            continue
        if(count==1):
            time = line.replace("时间:", "",1)
            count+=1
            # print (time)
            continue
        if(count>1):
            count+=1
            cotent+=line
            # print (line)
    cotent=cotent.replace("内容:","",1)
    # print (cotent)

    #========================================
    #      生成摘要
    #=======================================


    t = normal.zh2hans(cotent)
    sents = normal.get_sentences(t)
    doc = []
    for sent in sents:
        words = seg.seg(sent)
        words = normal.filter_stop(words)
        doc.append(words)
    rank = textrank.TextRank(doc)
    rank.solve()
    for index in rank.top_index(5):
        abstract=abstract+sents[index]+' '
        # print(sents[index])
    keyword_rank = textrank.KeywordTextRank(doc)
    keyword_rank.solve()
    keywords={}
    word0={}
    word1={}
    word2={}
    word3 = {}
    word4 = {}
    wordcount=0
    for w in keyword_rank.top_index(5):
        if(wordcount==0):
           word0["word"]=w
           word0["frequency"]=cotent.count(w)

        if (wordcount == 1):
            word1["word"] = w
            word1["frequency"] = cotent.count(w)
        if (wordcount == 2):
            word2["word"] = w
            word2["frequency"] = cotent.count(w)
        if (wordcount == 3):
            word3["word"] = w
            word3["frequency"] = cotent.count(w)
        if (wordcount == 4):
            word4["word"] = w
            word4["frequency"] = cotent.count(w)
        wordcount+=1

        # print(w)
        # print (cotent.count(w))
    s=SnowNLP(cotent)
    # print (s.sentiments)
    score=(s.sentiments-0.5)*2
    import json

    keywords=[word0,word1,word2,word3,word4]
    result={}
    result["code"]=1
    result["message"]="sucess"
    result["tilte"]=title
    result["time"]=time
    result['abstract']=abstract
    result['sentiment']=score
    result["keywords"]=keywords


    data={}
    data[""+filename]=result

    jsonStr = json.dumps(data)

    print (jsonStr)