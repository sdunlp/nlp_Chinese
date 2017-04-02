#coding=utf-8
import os
import chardet
import sys
reload(sys)
f=open('./News','r')
f_read=f.read()
f_charInfo=chardet.detect(f_read)
print f_charInfo
