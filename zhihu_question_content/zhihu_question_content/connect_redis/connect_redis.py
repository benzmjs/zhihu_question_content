from zhihu_question_content.settings import THIRD_REDIS_HOST, THIRD_REDIS_PORT, THIRD_REDIS_DB, THIRD_REDIS_PASSWORD
import redis


class ConnectRedis:
    def __init__(self):
        self.pool = redis.ConnectionPool(host=THIRD_REDIS_HOST, port=THIRD_REDIS_PORT, db=THIRD_REDIS_DB,
                                         password=THIRD_REDIS_PASSWORD)
        self.connect_redis = redis.StrictRedis(connection_pool=self.pool)

    def return_connect_redis(self):
        return self.connect_redis
