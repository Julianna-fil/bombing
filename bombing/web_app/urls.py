from django.urls import path
from django.conf.urls import url

from . import views
from .views import index, information

app_name = 'web_app'
urlpatterns = [
    #url(r'^time/$', views.today_is, name='time'),
    #path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('information/', information, name='information'),
]