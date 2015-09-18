# coding:utf-8

import urllib
import re
from bs4 import BeautifulSoup

class tianji(object):

    rooturlset = ['http://pic.yesky.com/256/36529756.shtml','http://pic.yesky.com/496/97556496.shtml',
                    'http://pic.yesky.com/163/85383663.shtml','http://pic.yesky.com/299/51285299.shtml',
                    'http://pic.yesky.com/233/54594733.shtml']
    urld = []

    def __init__(self,rooturl = None):
        if rooturl != None:
            self.rooturlset.insert(0,rooturl)


    def Info(self,pageurl):
        ''' imgurl: the current img url, pageurl: the next page url. '''

        response = urllib.urlopen(pageurl)
        if response.getcode() == 200 :
            soup = BeautifulSoup(response.read(),'html.parser')
            tag1 = soup.find('div',class_ = "l_effect_img_mid")
            imgurl = tag1.a.img.attrs['src']
            tag2 = soup.find('a',class_ = "effect_img_right")
            pageurl = tag2.attrs['href']
            return {'pageurl':pageurl,'imgurl':imgurl}
        else:
            return None


    def Download(self,pageurl):

        firstname = re.search(r'([\d_]*)\.shtml$',pageurl).group(1)
        pre_name = None
        n = 1
        while (firstname != pre_name) or (n == 2) :   
            info = self.Info(pageurl)
            if info == None :
                return 1
            imgurl = info['imgurl']

            pre_name = re.search(r'([\d_]*)\.shtml$',pageurl).group(1)
            suf_name = re.split(r'\.',imgurl)[-1]
            filename = 'E:\MyPython\img\\' + pre_name + '.' + suf_name

            urllib.urlretrieve(imgurl,filename)

            pageurl = info['pageurl']
            print n
            n += 1
        return firstname


    def Main(self):
        
        rooturl = self.rooturlset[0]
        firstname = self.Download(rooturl)
        if firstname == 1 :
            rooturl = self.rooturlset[1]
            firstname = self.Download(rooturl)
            if firstname == 1 :
                rooturl = self.rooturlset[2]
                firstname = self.Download(rooturl)
        else:
            self.urld.append(firstname)

        while True:
            html = urllib.urlopen(rooturl).read()
            soup = BeautifulSoup(html,'html.parser')
            tag_div_xgtjtj = soup.find('div',class_ = 'xgtjtj')
            tag_dl = tag_div_xgtjtj.dl
            nexturl = tag_dl.dt.a.attrs['href']
            print nexturl
            while True:
                print 'start while2'
                firstname = re.search(r'([\d_]*)\.shtml$',nexturl).group(1)
                print 'firstname:',firstname
                if firstname not in self.urld:
                    result = self.Download(nexturl)
                    if result == 1 :
                        nexturl = tag_dl.next_sibling.next_sibling.a.attrs['href']
                    else:
                        self.urld.append(result)
                        rooturl = nexturl
                        break
                else:
                    nexturl = tag_dl.next_sibling.next_sibling.a.attrs['href']
                    

      


img = tianji()
img.Main()