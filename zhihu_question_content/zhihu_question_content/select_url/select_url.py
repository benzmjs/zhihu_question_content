import pymysql
from zhihu_question_content.settings import URL_MYSQL_HOST, URL_MYSQL_USER, URL_MYSQL_PASSWORD, URL_MYSQL_TABLE


class Select_Mysql:
    def __init__(self):
        self.conn = pymysql.connect(host=URL_MYSQL_HOST, user=URL_MYSQL_USER, password=URL_MYSQL_PASSWORD,
                                    database=URL_MYSQL_TABLE, charset="utf8")
        self.cursor = self.conn.cursor()

    def select_url(self):
        select_sql = """
        SELECT url from high_heat_url;
        """
        self.cursor.execute(select_sql)
        all_url_tuple = self.cursor.fetchall()
        for every_url in all_url_tuple:
            yield every_url[0]
        self.cursor.close()
        self.conn.close()




