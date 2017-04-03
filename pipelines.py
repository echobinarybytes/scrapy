# -*- coding: utf-8 -*-




import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class Sina01Pipeline(object):
 #  def process_item(self, item, spider):
  #      print(spider.name)
   #     return item


#from twisted.enterprise import adbapi  # 导入twisted的包
#import MySQLdb
#import MySQLdb.cursors


#class Sina01Pipeline(object):
 #   def __init__(self):  # 初始化连接mysql的数据库相关信息
  #      self.dbpool = adbapi.ConnectionPool('MySQLdb',
   #                                         db='sina',
    #                                        user='huangxin',
     #                                       passwd='huangxin19960828',
    #                                        cursorclass=MySQLdb.cursors.DictCursor,
   #                                         charset='utf8',
  #                                          use_unicode=False
 #                                           )
#
        # pipeline dafault function                    #这个函数是pipeline默认调用的函数

    #def process_item(self, item, spider):
     #   query = self.dbpool.runInteraction(self._conditional_insert, item)
    #    return item

        # insert the data to databases                 #把数据插入到数据库中

   # def _conditional_insert(self, tx, item):
        #sql = "insert into book values (%s, %s)"
        #tx.execute(sql, (item["title"], item["time"],item["content"],item["urls"]))
#print 'abcdefghijkmnopq'

# -*- coding: utf-8 -*-
from twisted.enterprise import adbapi  # 导入twisted的包
import MySQLdb
#import MySQLdb.cursors
class Sina01Pipeline(object):
    def process_item(self, item, spider):
        conn = MySQLdb.connect(host='localhost', user='root', passwd='passwd', db='film',charset = "utf8")  # 连接数据库
        cursor = conn.cursor()
        sql = "insert into sina(title,content,time) values(%s,%s,%s)"
#cur.execute('create table activecode(id int,name varchar(20))')  # 创建数据表
#cur.executemany('insert into activecode values(%s,%s)', (34,'bbb'))  # 向数据表中插入数据
        param = (item['title'].encode('utf-8'),item['content'].encode('utf-8'),item['time'].encode('utf-8'))
        n = cursor.execute(sql,param)
        print n
        conn.commit()  # 提交事务
#cur.close()  # 关闭操作游标
        conn.close()  # 关闭数据库连接
