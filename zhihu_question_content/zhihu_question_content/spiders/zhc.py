# -*- coding: utf-8 -*-
import scrapy
import json
import re
import hashlib
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



    def sha1(self, before_sha_unlabeled_content):
        sha1obj = hashlib.sha1()
        sha1obj.update(before_sha_unlabeled_content.encode('utf-8'))
        after_sha_unlabeled_content = sha1obj.hexdigest()
        return after_sha_unlabeled_content



