### 1. start django( /ˈdʒæŋɡoʊ/)  
#### 查看django版本  
> python -m django --version  
#### 安装django  
> pip install django  
#### 升级django  
> python -m pip install --upgrade pip  
> pip install --upgrade django  
#### 卸载django  
> pip uninstall django  
#### 创建项目  
在指定文件夹下  
> django-admin startproject mysite  

\* 其中mysite为项目名，避免使用 Python 或 Django 的内部保留字来命名你的项目  
目录结构如下：  
>     mysite/  
>         manage.py  
>         mysite/  
>             __init__.py  
>             settings.py  
>             urls.py  
>             wsgi.py  

- 最外层的 mysite/ 根目录只是你项目的容器，可以随意修改。  
- manage.py: 一个让你用各种方式管理 Django 项目的命令行工具。  
- 里面一层的 mysite/ 目录包含你的项目，它是一个纯 Python 包。  
- mysite/__init__.py：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。  
- mysite/settings.py：Django 项目的配置文件。  
- mysite/urls.py：Django 项目的 URL 声明。  
- mysite/wsgi.py：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。  

#### 用于开发的简易服务器  
进入项目路径下  
> python manage.py runserver  
#### 创建应用  
> python manage.py startapp newapp  

目录结构如下：  
>     newapp/  
>         __init__.py  
>         admin.py  
>         apps.py  
>         migrations/  
>             __init__.py  
>         models.py  
>         tests.py  
>         views.py  

### 2. backend  
#### 数据库配置  
打开`mysite/settings.py`  
DATABASES  
  - ENGINE:  
    'django.db.backends.sqlite3'，'django.db.backends.postgresql'，'django.db.backends.mysql'，或 'django.db.backends.oracle'  
  - NAME: 数据库的名称  
  - USER: 用户名  
  - PASSWORD: 密码  
  - HOST: 主机  
  - PORT: 端口  

#### 时区设置  
LANGUAGE_CODE = 'zh-hans'  
TIME_ZONE = 'Asia/Shanghai'  

#### INSTALLED_APPS  
- django.contrib.admin -- 管理员站点。  
- django.contrib.auth -- 认证授权系统。  
- django.contrib.contenttypes -- 内容类型框架。  
- django.contrib.sessions -- 会话框架。  
- django.contrib.messages -- 消息框架。  
- django.contrib.staticfiles -- 管理静态文件的框架。  

数据库迁移：  
> python manage.py migrate  

添加自己的应用：  
'portal.apps.PortalConfig',
#### 创建模型  
\* 型是真实数据的简单明确的描述。它包含了储存的数据所必要的字段和行为  
迁移:  
> python manage.py makemigrations portal  
查看迁移sql：  
> python manage.py sqlmigrate portal 0001  

#### Django 管理页面  
##### 创建管理员账号  
> python manage.py createsuperuser  

##### 向管理页面中加入  
`portal/admin.py`  
>     from .models import News
>     admin.site.register(News)












