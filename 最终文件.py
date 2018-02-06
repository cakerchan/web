# -*- coding: utf-8 -*-
import re
import HTMLParser
import pandas as pd
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree

path = "/home/caker/dpcl"
files = os.listdir(path)
'''
#修改文件名字
string = string.printable
sz = string[:10]
zm = string[10:62]
x = 0
for file in files:
    x += 1
    fname = random.choice(zm) + str(x + 0) + random.choice(zm)
    if not os.path.isdir(file):
        fp = path + '/' + file
        ak = file.split('.')[-1]
        nfname = fname + '.' + ak
        fpp = path + '/' + nfname
        os.rename(fp, fpp)
        print fp
        print fpp
'''
#统计信息条数
def rdfile(path):
    list = []
    list2 = []
    files = os.listdir(path)
    x = 0
    for file in files:
        x += 1
        print '第', x, '页'
        if not os.path.isdir(file):
            fp = path + '/' + file
            f = open(fp)
            aaa = f.read()
            xm = etree.HTML(aaa)
            w = xm.xpath('//div[@class="main-review"]')
            if not w:
                print 'ok,meiyou'
            else:
                y = 0
                for kks in w:
                    y += 1
                    print '第', y, '条'
                    jm = etree.tostring(kks)
                    h = HTMLParser.HTMLParser()
                    nr = h.unescape(jm)
                    sc = re.sub('<a class="name.*?>', 'shanchuba', nr)
                    name = re.findall('(?<=shanchuba)[\s\S]*?(?=</a>)', sc)
                    names = ''.join(name).strip()
                    list.append(names)
                    des1 = re.findall('(?<=<div class="review-words Hide">)[\s\S]*?(?=<div class="less-words">)', nr)
                    des2 = re.findall('(?<=<div class="review-words">)[\s\S]*?(?=</div>)', nr)
                    if not des1:
                        des = ''.join(des2).strip()
                        list2.append(des)
                    else:
                        des = ''.join(des1).strip()
                        list2.append(des)
                data = pd.DataFrame({'NAME': list, 'DES': list2})
                data.to_csv("/home/caker/dianping.csv", index=False, sep=',')
            f.close()
    t = 0
    for m in list:
        t +=1
    print '共 ',x,' 页 ',t,' 条'
if __name__ == "__main__":
    path = "/home/caker/dpcl"
    rdfile(path)