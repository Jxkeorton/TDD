from django.urls import path
from lists import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home_page, name='home'),
    path('<int:list_id>/', views.view_list, name='view_list'),
    path('new', views.new_list, name='new_list'),
    path('<int:list_id>/add_item', views.add_item, name="add_item"),
]
