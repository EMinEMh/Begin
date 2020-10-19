from django.conf.urls import url
from django.urls import path
from accounts import views

app_name = "account"

urlpatterns = [
    url(r'^login/$',views.LoginView.as_view(),name='login',),
]