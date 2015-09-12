#coding:utf-8

import urllib2
import re
import sys
reload (sys)
sys.setdefaultencoding('utf8')  


class budejie(object):
    """docstring for budejie"""

    def __init__(self):

        self.encoding = sys.getfilesystemencoding()
        self.content = self.GetContent()

    def LoadPage(self):
        '''Return the html code. '''

        url = 'http://www.budejie.com/duanzi/'
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
        header = {'User-Agent' : user_agent}
        request = urllib2.Request(url,headers = header)

        try:
            hpage = urllib2.urlopen(request)
            return hpage.read().decode('utf-8').encode(self.encoding)
        except urllib2.URLError as e:
            if hasattr(e,'code'):
                print e.code
            if hasattr(e,'reason'):
                print e.reason
            return None
        finally:
            hpage.close()

        
    def GetContent(self):
        '''Put the username,releasetime,content,lovenum into a list. '''

        html = self.LoadPage()
        pattern = re.compile(r'''<li class=['"]user_name['"]>\s*<p>(.*)</p>\s*</li>\s*'''  #user_name
                            +r'''<li>\s*<p class=['"]time['"]>(.*)</p>\s*</li>\s*</ul>\s*</div>\s*'''     #ReleaseTime
                            +r'''.*\s*<div class=['"]post-body['"]>\s*<p.*>\s*(.*)\s*</p>\s*</div>\s*'''   #Content
                            +r'''<div class=['"]budejie_mutual clear['"]>\s*.*\s*<li>\s*<a.*>\s*<span.*>(.*)</span>'''  #LoveNum
                            )
        return re.findall(pattern,html)


    def Print(self):
        '''Print the result from function GetContent. '''

        items = self.content
        for item in items :
            print u'发布人: ',item[0]
            print item[1]
            print u'内容: ',item[2]
            print u'点赞数: ',item[3]
            print '-'*40


    def Record(self,filename='E:\MyPython\\budejie.txt'):
        '''Write the result from function GetContent into a file. 
           file:"E:\MyPython\\budejie.txt" is default. '''

        items = self.content
        with open(filename,'w') as f:
            for item in items:
                f.write(u'发布人: '+item[0].decode(self.encoding)+'\n')
                f.write(item[1].decode(self.encoding)+'\n')
                f.write(u'内容: '+item[2].decode(self.encoding)+'\n')
                f.write(u'点赞数: '+item[3].decode(self.encoding)+'\n')
                f.write('-'*40+'\n')

        print 'ok'


if __name__ == '__main__' :
    jie = budejie()
    jie.Print()
    jie.Record()
