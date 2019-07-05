from django.db import models, connection

# Create your models here.
class News(models.Model):
  news_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
  news_title = models.CharField(max_length=200)
  news_source = models.CharField(max_length=50)
  news_content = models.TextField(default="")
  publish_time = models.DateTimeField(null=True)
  news_status = models.CharField(max_length=2,default="0")
  create_time = models.DateTimeField(auto_now=True)
  update_time = models.DateTimeField(null=True)

  def __str__(self):
        return self.news_title

  
  def getNewsByNewsId(news_id):
    sql = 'SELECT * FROM portal_news WHERE news_id=%s'
    params = list()
    params.append(news_id)
    dao = DaoSupport()
    return dao.selectOne(sql,params)

  def getNewsList(params=None):
    condition = params[0]

    news_status = condition.get('news_status')

    selectsql = " SELECT news_id,news_title,news_source,news_content,date_format(publish_time, '%%Y-%%m-%%d %%H:%%i:%%s') "
    fromsql = " FROM portal_news WHERE 1 = 1 "
    if news_status is not None:
      fromsql += " AND news_status = %s "
    dao = DaoSupport()
    return dao.selectPagination(selectsql, fromsql, params)

class DaoSupport(object):

  def selectOne(self,sql,params):
    with connection.cursor() as cursor:
      cursor.execute(sql,params)
      row = cursor.fetchone()
    return row

  def selectList(self,sql,params):
    with connection.cursor() as cursor:
      cursor.execute(sql,params)
      row = cursor.fetchall()
    return row
  '''
    分页查询 字段类型为 数字或字符串  如有datetime等格式 需进行格式转化

  '''
  def selectPagination(self,selectsql,fromsql,params):
    countsql = ' SELECT COUNT(1) '
    pagesql = ' limit %s, %s'
    condition = params[0]

    conditionparams = [condition.get(k) for k in condition]

    with connection.cursor() as cursor:
      if len(conditionparams) == 0:
        cursor.execute(countsql + fromsql)
      else:
        cursor.execute(countsql + fromsql,conditionparams)
      row = cursor.fetchone()
      total_count = row[0]
      
      sql = selectsql + fromsql + pagesql
      print('sql:%s,params:%s' % (sql,params))
      
      page = Page(total_count,params[-2],params[-1])
      params[-2] = page.current_index
      conditionparams.append(params[-2])
      conditionparams.append(params[-1])
      cursor.execute(sql,conditionparams)
      rows = cursor.fetchall()
      page.setRows(rows)

    return page.to_dict()

class Page(object):
  # 总数量total_count
  # 当前页current_page
  # 每页显示个数pagenum
  # 当前索引current_index
  # 总页数total_page
  # 列表rows
  def __init__(self, total_count, current_page, pagenum):
    self.total_count = total_count
    self.total_page = (total_count+pagenum-1)//pagenum
    self.current_page = 1 if current_page <= 0 else ( self.total_page if current_page > self.total_page else current_page)
    self.pagenum = pagenum
    self.current_index = (current_page-1)*pagenum

  def setRows(self, rows):
    self.rows = rows

  def to_dict(self):
    dict = {}
    dict.update(self.__dict__)
    return dict


    