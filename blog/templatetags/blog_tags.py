from django import template

register = template.Library()

@register.inclusion_tag('blog/tags/article_info.html')
def load_article_detail(article, isindex, user):
    """
    加载文章详情
    :param article:
    :param isindex:是否列表页，若是列表页只显示摘要
    :return:
    """
    # from Begin.utils import get_blog_setting
    # blogsetting = get_blog_setting()

    return {
        'article': article,
        'isindex': isindex,
        'user': user,
        # 'open_site_comment': blogsetting.open_site_comment,
    }