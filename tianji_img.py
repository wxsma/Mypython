# coding:utf-8

import urllib
import re
from bs4 import BeautifulSoup

url = 'http://pic.yesky.com/256/36529756.shtml'



def Info(pageurl):
    ''' imgurl: the current img url, pageurl: the next page url. '''

    response = urllib.urlopen(pageurl)
    if response.getcode() == 200 :
        soup = BeautifulSoup(response.read(),'html.parser')
        tag1 = soup.find('div',class_ = "l_effect_img_mid")
        imgurl = tag1.a.img.attrs['src']
        tag2 = soup.find('a',class_ = "effect_img_right")
        pageurl = tag2.attrs['href']
        return {'pageurl':pageurl,
                'imgurl':imgurl}
    else:
        return None

def LoopStoper(pageurl):

    firstname = re.search(r'([\d_]*)\.shtml$',pageurl).group(1)
    pre_name = None
    n = 1
    while (firstname != pre_name) or (n == 2) :   
        info = Info(pageurl)
        if info == None :
            return 'the info in None. '
        imgurl = info['imgurl']

        pre_name = re.search(r'([\d_]*)\.shtml$',pageurl).group(1)
        suf_name = re.split(r'\.',imgurl)[-1]
        filename = 'E:\MyPython\img\\' + pre_name + '.' + suf_name

        urllib.urlretrieve(imgurl,filename)

        pageurl = info['pageurl']
        print n
        n += 1

    return 0





