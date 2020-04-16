from django.conf.urls import url
from .views import *

app_name = 'webview'

urlpatterns = [
    url(r'^index/$', index_view),
]