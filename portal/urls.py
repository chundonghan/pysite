from django.urls import path

from . import views
# 设置命名空间
app_name = 'portal'
urlpatterns = [
    path('', views.index, name='index'),
    path('news/<int:news_id>/', views.detail, name='new_detail'),
    path('news/list/<int:page>/<int:pagenum>/', views.listing, name='new_list'),
    
]