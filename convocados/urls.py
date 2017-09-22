from django.conf.urls import url
from . import views

app_name = 'convocados'

urlpatterns = [
    # /convocados/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /convocados/3
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]