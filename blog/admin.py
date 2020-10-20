from django.contrib import admin

# Register your models here.
from blog.models import Article



class ArticlelAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'author',
        'views',
        'status',
        'type',)





admin.site.register(Article,ArticlelAdmin)