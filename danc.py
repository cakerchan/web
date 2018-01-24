import urllib2
import re
from lxml import etree



url = 'http://physicsworld.com/cws/article/news/2015/sep/23/how-to-put-neutrons-into-a-twist'
m = urllib2.urlopen(url).read()
xm = etree.HTML(m)
kk = xm.xpath('//div[@class="articleBody"]')
for kks in kk:
    html = etree.tostring(kks)
    klss = re.sub('((?<=src=")(.*?)(?=/[^/]*"))', 'http://www.actualites-les.com/static/images/phy', html)
    datas1 = re.sub('<a.*?">', '', klss)
    data2 = re.sub('</a>', '', datas1)
    print data2

#kl = re.sub('(?<=src=")(.*?)(?=/[^/]*$)','http://www.actualites-les.com/static/images/phy',url)

#kls = 'http://www.actualites-les.com/static/images/phy' + kl
#klss = re.sub('((?<=src=")(.*?)(?=/[^/]*"))','http://www.actualites-les.com/static/images/phy',url)
#print klss


