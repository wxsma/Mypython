# coding:utf-8

import urllib2
import urllib
# from bs4 import BeautifulSoup
import re
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class jwc(object):
    """docstring for jwc"""

    def LoadPage(self,url = 'http://jwc.hqu.edu.cn/'):
        ''' Open a link, return a dictionary containing respones and html'''

        header = {'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
                  'Host':'jwc.hqu.edu.cn'
                 }
        request = urllib2.Request(url,headers = header)

        try:
            respones = urllib2.urlopen(request)
        except urllib2.URLError as e:
            if hasattr(e,'code'):
                print e.code
            if hasattr(e,'reason'):
                print e.reason
            return None
        else:
            html = respones.read()

            # Find the urlpage's encoding.
            pattern = r'<meta.*charset=(.*)">'
            encoding = re.search(pattern,html).group(1)

            html = html.decode(encoding).encode('utf-8')
            return {'respones':respones,'html':html}
        finally:
            respones.close()

    def Notice(self,url):

        html = self.LoadPage()['html']
        


j = jwc()
html = j.LoadPage()['html']
