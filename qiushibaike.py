# coding:utf-8
# 采集糗事百科段子
#
# 
import urllib2
import re


class Qiushibaike(object):
    """docstring for Qiushibaike"""
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
        self.headers = {'User-Agent': self.user_agent}
        self.enable = False

    def getcode(self, num):
        for i in xrange(1, num+1):
            print '----------------------------------第%d页--------------------------------' % i
            url1 = 'http://www.qiushibaike.com/8hr/page/'
            url2 = '/?s=4964586'
            url = url1 + str(num) + url2

            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            page_code = response.read()
            # print page_code
            # 正则
            pattern = re.compile(
                '<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?' +
                '<span class="stats-vote">.*?<i class="number">(.*?)</i>.*?' +
                '<span class="stats-comments">.*?<i class="number">(.*?)</i>', re.S)
            items = re.findall(pattern, page_code)

            # 输出爬去到的内容
            for item in items:
                # 优化正则
                replace = re.compile('<br/>')
                text = re.sub(replace, "\n", item[1])
                text = text[10:-10]
                print '作者:', item[0], '点赞数:', item[2], '评论数:', item[3]
                print '段子:', text, "\n"

    def start(self):
        self.enable = True
        num = int(raw_input('请输入要看多少页:'))
        self.getcode(num)


spider = Qiushibaike()
spider.start()
