# -*- coding:utf8 -*-
import urllib

if __name__ == '__main__':
    url_get_base = "http://api.ltp-cloud.com/analysis/"
    text='''我是中国人。我爱我的祖国。
    '''
    args = {
        'api_key' : 'h8p5s6n0onDR9r3O2FkQdrFuPMUX6HyvnthFbFPP',
        'text' : text,
        'pattern' : 'ws',
        'format' : 'plain'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args)) # POST method
    content = result.read().strip()
    # list1=content.encode('utf-8').split(' ')
    print content


