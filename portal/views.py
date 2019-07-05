from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from django.utils import timezone

from portal.models import News
import json
# Create your views here.
def index(request):
  template = loader.get_template('portal/index.html')
  context = {'title':'门户首页'}
  # try:
  #   1/0
  # except Exception:
  #   raise Http404("Question does not exist")

  # return HttpResponse(template.render(context, request))
  return render(request, 'portal/index.html', context)

def listing(request,page,pagenum):
  condition = {}
  s = request.GET.get('s')
  if s is not None:
    condition['news_status'] = s
  params = list()
  params.append(condition)
  params.append(page)
  params.append(pagenum)

  newsList = News.getNewsList(params)
  return JsonResponse(newsList,safe=False,json_dumps_params={'ensure_ascii':False})


def detail(request,news_id):
  news = News.getNewsByNewsId(news_id)
  return JsonResponse(news,safe=False,json_dumps_params={'ensure_ascii':False})



