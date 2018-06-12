# -*- coding:UTF-8 -*-
import urllib2
import re


class Spider:

    def __init__(self):
        self.enable = True
        self.page = 9
    """
    内涵段子爬虫
    """
    def loadPage(self, page):
        """
        定义一个url请求网页的方法
        :param page:返回需要请求的第几页
        :return:返回的页面
        """
        url = "http://www.neihan8.com/article/list_5_" + str(page)+".html"
        # User-Agent头
        user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0'
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req)
        html = response.read()
        gbk_html = html.decode('gbk').encode('utf-8')
        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
        item_list = pattern.findall(gbk_html)
        # print(item_list)
        # print(gbk_html)
        # return gbk_html
        return item_list

    def printOnePage(self, item_list, page):
        """
        @brief 处理得到的段子列表
        :param item_list: 得到的段子列表
        :param page: 处理第几页
        :return:
        """
        print("****** 第 %d 页 爬取完毕... *****" % page)
        for item in item_list:
            # print("=======")
            item = item.replace("<p>", "").replace("</p>", "").replace("<br />", "")
            # print(item)
            self.writeToFile(item)

    def writeToFile(self, text):
        """
        将数据追加写进文件中
        :param text: 文件内容
        :return:
        """
        myFile = open("./duanzi.txt", 'a')  # 追加形式打开文件
        myFile.write(text)
        myFile.write("----------------------")
        myFile.close()

    def doWork(self):
        """
        让爬虫开始工作
        :return:
        """
        # a = True
        while self.enable:
            try:
                item_list = self.loadPage(self.page)
            except urllib2.URLError, e:
                print(e.reason)
                continue
            item_list = self.loadPage(self.page)
                # 对得到的段子item_list处理
            self.printOnePage(item_list, self.page)
            self.page += 1
            print("按回车继续....")
            print("输入 quit 退出")
            command = raw_input()
            if command == "quit":
                self.enable = False
                break
        # pass

if __name__ == '__main__':
    """
        ======================
            内涵段子小爬虫
        ======================
    """

    print('请按下回车开始')
    raw_input()
    mySpider = Spider()

    # a = mySpider.loadPage(2)
    #
    # mySpider.printOnePage(a, 1)
    mySpider.doWork()