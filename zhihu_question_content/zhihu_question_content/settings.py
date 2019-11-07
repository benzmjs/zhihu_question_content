# -*- coding: utf-8 -*-

# Scrapy settings for zhihu_question_content project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu_question_content'

SPIDER_MODULES = ['zhihu_question_content.spiders']
NEWSPIDER_MODULE = 'zhihu_question_content.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihu_question_content.middlewares.ZhihuQuestionContentSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhihu_question_content.middlewares.ZhihuQuestionContentDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihu_question_content.pipelines.ZhihuQuestionContentPipeline': 299,
    # 'zhihu_question_content.pipelines.SaveImagePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
LOG_LEVEL = "WARNING"

# URL_MYSQL_HOST = '122.114.178.3'
# URL_MYSQL_USER = 'mjs'
# URL_MYSQL_PASSWORD = '123456'
# URL_MYSQL_TABLE = 'zhurl'

THIRD_REDIS_HOST = '122.114.178.3'
THIRD_REDIS_PORT = 7777
THIRD_REDIS_PASSWORD = 'v5jK8DJNprbo6siQIv'
THIRD_REDIS_DB = '0'

DATA_MYSQL_HOST = '122.114.121.137'
DATA_MYSQL_USER = 'ceshi_txglcz_com'
DATA_MYSQL_PASSWORD = 'jYRaEb3Mw4HKnDEy'
DATA_MYSQL_PORT = 3306
DATA_MYSQL_TABLE = 'ceshi_txglcz_com'

COOKIE = "tt_webid=6740907262875321864; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6740907262875321864; csrftoken=064366b260ef57098f50d408699e6a4a; _ga=GA1.2.757895929.1569548594; WIN_WH=375_812; UM_distinctid=16d94b0d176482-0ded3f44daf00f-6a12167a-1fa400-16d94b0d1774f3; CNZZDATA1259612802=1915830950-1570154940-https%253A%252F%252Fwww.toutiao.com%252F%7C1570344032; uuid='w:d76a1d08349142bc83bb5098ba066f1e'; __tasessionId=bm0s5te8y1571707377111; s_v_web_id=d00ce486f759d046acaf10441e8ae6a0"

# IMAGES_STORE = 'C:\\Users\\Administrator\\Desktop\\image'