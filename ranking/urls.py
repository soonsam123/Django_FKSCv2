from django.conf.urls import url
from . import views

app_name = 'ranking'

urlpatterns = [
    # /ranking/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /ranking/3
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]