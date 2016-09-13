from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'shoppingcart.views.home', name='home'),

    url(r'^store/', include('store.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
