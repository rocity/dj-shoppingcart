from django.conf.urls import url
from . import views

app_name = 'store'
urlpatterns = [
    url(r'^$', views.home, name='store_home'),
    url(r'^profile/$', views.profile, name='user_profile')
]
