# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time
import re
from zhihu_question_content.settings import DATA_MYSQL_HOST, DATA_MYSQL_USER, DATA_MYSQL_PASSWORD, DATA_MYSQL_PORT, \
    DATA_MYSQL_TABLE


class ZhihuQuestionContentPipeline(object):
    def __init__(self):
        # 连接MySQL
        self.connect = pymysql.connect(host=DATA_MYSQL_HOST, port=DATA_MYSQL_PORT, user=DATA_MYSQL_USER,
                                       password=DATA_MYSQL_PASSWORD,
                                       db=DATA_MYSQL_TABLE)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 将item数据写入表www_kaifamei_com_ecms_news_check
        insert_sql_first = '''INSERT INTO www_kaifamei_com_ecms_news_check(classid,newspath,filename,title,titleurl,newstime) VALUES (4,"{}","100","{}","news/yxnews/{}/{}","{}")'''.format(
            time.strftime('%Y-%m-%d', time.localtime(time.time())), item["title"],
            time.strftime('%Y-%m-%d', time.localtime(time.time())), '2.html', int(time.time()))
        update_sql_first = '''UPDATE www_kaifamei_com_ecms_news_check SET filename=id'''
        # 将item数据写入表www_kaifamei_com_ecms_news_check_data
        insert_sql_second = '''INSERT INTO www_kaifamei_com_ecms_news_check_data(classid,dokey,newstext) VALUES (4,1,'{}')'''.format(
            item["final_content"])
        # 将item数据写入表www_kaifamei_com_ecms_news_index
        insert_sql_third = '''INSERT INTO www_kaifamei_com_ecms_news_index(classid,lastdotime) VALUES (4,{})'''.format(
            int(time.time()))
        try:
            self.cursor.execute(insert_sql_first)
            self.cursor.execute(update_sql_first)
            self.cursor.execute(insert_sql_second)
            self.cursor.execute(insert_sql_third)
            self.connect.commit()
            print("插入数据库成功")
        except Exception as e:
            self.connect.rollback()
            print(e)
        return item

    # class SaveImagePipeline(ImagesPipeline):
    #
    #     def get_media_requests(self, item, info):
    #         for every_content_image_url in item["content_image_url"]:
    #             yield scrapy.Request('https://' + every_content_image_url)
    #
    #     def file_path(self, request, response=None, info=None):
    #         image_name = request.url.split('/')[-1]
    #         filename = u'{}'.format(image_name)
    #         return filename
