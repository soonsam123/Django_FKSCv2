from django.conf.urls import url
from . import views

app_name = 'inicial'

urlpatterns = [
    #
    url(r'^$', views.index, name='index'),
]