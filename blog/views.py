from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blog.models import LinkShowType, Article


class IndexView(ListView):
    '''
    首页
    '''
    link_type = LinkShowType.I

    def get_queryset_data(self):
        article_list = Article.objects.filter(type='a',status='p')
        return article_list
