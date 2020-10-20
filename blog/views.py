from django.core.cache import cache
from django.shortcuts import render
from django.views.generic import ListView
from Begin import settings
from blog.models import LinkShowType, Article
import logging

# Create your views here.

logger = logging.getLogger(__name__)


class ArticleListView(ListView):
    # template_name属性用于指定使用哪个模板进行渲染
    template_name = 'blog/article_index.html'

    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = 'article_list'

    # 页面类型，分类目录或标签列表等
    paginate_by = settings.PAGINATE_BY
    link_type = LinkShowType.L
    page_kwarg = 'page'
    # TODO 添加其他类型

    @property
    def page_number(self):
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        return page


    def get_queryset_cache_key(self):
        """
        子类重写 定义cache key
        """
        raise NotImplementedError

    def get_queryset_data(self):
        """
        子类重写get_queryset实现新的数据queryset
        """
        raise NotImplementedError

    def get_queryset_from_cache(self, cache_key):
        """
        定义cache key与value,先获取，获取不到则重新定义
        """
        value = cache.get(cache_key)
        if value:
            logger.info('get view cache.key:{key}'.format(key=cache_key))
            return value
        else:
            article_list = self.get_queryset_data()
            cache.set(cache_key, article_list)
            logger.info('set view cache.key:{key}'.format(key=cache_key))
            return article_list

    def get_queryset(self):
        """
        先从cache中获取
        """
        key = self.get_queryset_cache_key()
        value = self.get_queryset_from_cache(key)
        return value


class IndexView(ArticleListView):
    '''
    首页
    '''
    # 友情链接类型
    link_type = LinkShowType.I

    def get_queryset_data(self):
        article_list = Article.objects.filter(status='p',type='a')
        return article_list

    def get_queryset_cache_key(self):
        cache_key = 'index_{page}'.format(page=self.page_number)
        return cache_key




