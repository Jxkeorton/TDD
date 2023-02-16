
from django.urls import path
from lists import views as list_views
from lists import urls as list_urls
from django.conf.urls import include, url

urlpatterns = [
    path('', list_views.home_page, name='home'),
    path('lists/', include(list_urls)),
]
