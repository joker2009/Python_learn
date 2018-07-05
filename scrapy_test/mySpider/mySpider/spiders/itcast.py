# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    # start_urls = ['http://itcast.cn/']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # pass
        # with open("teachers.html", "w") as f:
        #     f.write(response.text)
        #
        # 存放老师信息的合集
        items = []

        for each in response.xpath("//div[@class='li_txt']"):
            # 将我们得到的数据封装成一个‘ItcastItem’对象
            item = ItcastItem()
            # extract()方法返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            # xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            yield item
        #     items.append(item)
        # print(items)
        # return items


