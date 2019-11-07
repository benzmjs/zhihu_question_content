# -*- coding: utf-8 -*-
import scrapy
import json
import re
import hashlib
import random
from zhihu_question_content.select_url.select_url import Select_Mysql
from zhihu_question_content.connect_redis.connect_redis import ConnectRedis
from zhihu_question_content.settings import COOKIE
from zhihu_question_content.items import ZhihuQuestionContentItem


class ZhcSpider(scrapy.Spider):
    # select_mysql_object = Select_Mysql()
    name = 'zhc'
    start_urls = [
        "https://www.zhihu.com/api/v4/questions/46349433/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset=3&limit=5&sort_by=default&platform=desktop"]

    def parse(self, response):
        item = ZhihuQuestionContentItem()
        dict_data = json.loads(response.body.decode())
        question_list = dict_data["data"]
        for every_question in question_list:
            item["tagged_content"] = every_question["content"]
            labeled = re.compile(r'<[^>]+>', re.S)
            item["unlabeled_content"] = labeled.sub('', item["tagged_content"])
            item["title"] = every_question["question"]["title"]
            item["content_image_url"] = re.findall(r'https://(.*?)"', item["tagged_content"])
            item["final_content"] = self.replace_content_url(item["tagged_content"], item["content_image_url"])
            re_str=re.compile(r'<img\b[^>]*>',re.S)
            item["final_content"]=re_str.sub('',item["final_content"])
            after_sha1_content = self.sha1(item["unlabeled_content"])
            if not self.estimate_exists(after_sha1_content) and len(item["unlabeled_content"]) > 25:
                ten_word_list = self.random_choice_ten_word(item["unlabeled_content"])
                for every_word in ten_word_list:
                    item["marked"] = False
                    yield scrapy.Request(
                        url='https://www.baidu.com/s?wd={}'.format(every_word),
                        callback=self.original_sentence_analysis,
                        meta={"item": item}
                    )
        next_url = dict_data["paging"]["next"]
        if not dict_data["paging"]["is_end"]:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def replace_content_url(self, content, content_image_url):
        for every_content_url in content_image_url:
            content = content.replace(r'https://' + every_content_url, '')

        return content

    def sha1(self, before_sha_unlabeled_content):
        sha1obj = hashlib.sha1()
        sha1obj.update(before_sha_unlabeled_content.encode('utf-8'))
        after_sha_unlabeled_content = sha1obj.hexdigest()
        return after_sha_unlabeled_content

    def estimate_exists(self, after_sha1_content):
        content_redis_object = ConnectRedis()
        start_count = content_redis_object.connect_redis.scard('content')
        content_redis_object.connect_redis.sadd('content', after_sha1_content)
        end_count = content_redis_object.connect_redis.scard('content')
        if start_count != end_count:
            return False
        else:
            return True

    def random_choice_ten_word(self, unlabeled_content):
        count = 0
        ten_word_list = []
        while count < 10:
            start_index = random.randint(0, len(unlabeled_content) - 25)
            every_str_word = unlabeled_content[start_index:(start_index + 25)]
            ten_word_list.append(every_str_word)
            count += 1
        return ten_word_list

    def original_sentence_analysis(self, response):
        item = response.meta["item"]
        self.num = 0
        result_str = ''.join(
            response.xpath('//*[@id=1]//div[@class="c-abstract"]//em/text()').extract())
        if len(result_str) < 15:
            self.num = self.num + 1

        if self.num >= 7:
            if not item["marked"]:
                item["title"] = "(原创)" + item["title"]
                item["marked"] = True
                yield item

        else:
            str_content = self.random_choice_one_word(item["unlabeled_content"])
            yield scrapy.Request(
                url='http://www.baidu.com/s?wd={}'.format(str_content),
                callback=self.quality_analysis,
                meta={"item": item}
            )

    def random_choice_one_word(self, str_content):
        start_index = random.randint(0, len(str_content) - 25)
        every_str_word = str_content[start_index:start_index + 25]
        return every_str_word

    def quality_analysis(self, response):
        item = response.meta["item"]
        self.red_content_num = 0
        for id_num in range(1, 11):
            result_str = ''.join(
                response.xpath('//*[@id="{}"]//div[@class="c-abstract"]//em/text()'.format(id_num)).extract())
            if len(result_str) >= 25:
                self.red_content_num = self.red_content_num + 1
        if 0 < self.red_content_num < 3 and not item["marked"]:
            item["marked"] = True
            item["title"] = "(非原创优质)" + item["title"]
            yield item
        if 2 < self.red_content_num < 6 and not item["marked"]:
            item["marked"] = True
            item["title"] = "(非原创中等)" + item["title"]
            yield item

        if 5 < self.red_content_num < 9 and not item["marked"]:
            item["marked"] = True
            item["title"] = "(非原创一般)" + item["title"]
            yield item
        if 8 < self.red_content_num < 11 and not item["marked"]:
            item["marked"] = True
            item["title"] = "(非原创最差)" + item["title"]
            yield item
