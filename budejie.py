#  coding:utf-8

import urllib2
import re

url = 'http://www.budejie.com/duanzi/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
header = {'User-Agent' : user_agent}

request = urllib2.Request(url,headers = header)
hpage = urllib2.urlopen(request)
html = hpage.read()
                        
pattern = re.compile(r'''<li class=['"]user_name['"]>\s*<p>(.*)</p>\s*</li>\s*'''  #user_name
                    +r'''<li>\s*<p class=['"]time['"]>(.*)</p>\s*</li>\s*</ul>\s*</div>\s*'''     #ReleaseTime
                    +r'''.*\s*<div class=['"]post-body['"]>\s*<p.*>\s*(.*)\s*</p>\s*</div>\s*'''   #Content
                    +r'''<div class=['"]budejie_mutual clear['"]>\s*.*\s*<li>\s*<a.*>\s*<span.*>(.*)</span>'''  #LoveNum
                    )
items = re.findall(pattern,html)
# for item in items :
#     print u'发布人: ',item[0]
#     print item[1]
#     print u'内容: ',item[2]
#     print u'点赞数: ',item[3]
#     print '-'*40
# print '-'*70
# print len(items)

with open('budejie.txt','w') as file_budejie:
    for item in items:
        file_budejie.write(u'发布人: '+item[0]+'\n')
        file_budejie.write(item[1]+'\n')
        file_budejie.write(u'内容: '+item[2]+'\n')
        file_budejie.write(u'点赞数: '+item[3]+'\n')
        file_budejie.write('-'*40+'\n')

hpage.close()