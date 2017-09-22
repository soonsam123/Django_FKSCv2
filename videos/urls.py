from django.conf.urls import url
from . import views

app_name = 'videos'

urlpatterns = [
    # /videos/
    url(r'^$', views.index, name='index'),
]