# -*- coding: utf-8 -*-
import scrapy
import json
import re
import hashlib
import random
from zhihu_question_content.select_url.select_url import Select_Mysql
from zhihu_question_content.connect_redis.connect_redis import ConnectRedis


class ZhcSpider(scrapy.Spider):
    select_mysql_object = Select_Mysql()
    name = 'zhc'
    allowed_domains = ['www.zhihu.com']
    start_urls = [
        "https://www.zhihu.com/api/v4/questions/46349433/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset=3&limit=5&sort_by=default&platform=desktop"]

    def parse(self, response):
        dict_data = json.loads(response.body.decode())
        question_list = dict_data["data"]
        for every_question in question_list:
            tagged_content = every_question["content"]
            labeled = re.compile(r'<[^>]+>', re.S)
            unlabeled_content = labeled.sub('', tagged_content)
            title = every_question["question"]["title"]
            after_sha1_content = self.sha1(unlabeled_content)
            if not self.estimate_exists(after_sha1_content):
                # 判断原创性，写入数据库
                ten_word_list = self.random_choice_ten_word(unlabeled_content)
                self.judge_content_whether_original(ten_word_list)
            next_url = dict_data["paging"]["next"]
            if not dict_data["paging"]["is_end"]:
                yield scrapy.Request(
                    next_url,
                    callback=self.parse
                )

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
            every_str_word = unlabeled_content[start_index:start_index + 25]
            ten_word_list.append(every_str_word)
            count += 1
        return ten_word_list

    def judge_content_whether_original(self,ten_word_list):
        i=0
        for every_one_word in ten_word_list:
            print(every_one_word)
            print(i)
            i+=1
        print("==="*60)