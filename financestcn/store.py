#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_stcnDB = client[settings['MONGODB_DB']]
collect_stcn_161212 = News_stcnDB[settings['MONGODB_COLLECTION']]