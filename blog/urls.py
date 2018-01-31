
from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index),
    path('article/<int:article_id>',views.article_page),
    path('article/add_page/',views.add_page),
    path('article/add_page_action',views.add_page_action),
    path('article/edit_page/<int:article_id>',views.edit_page),
    path('article/edit_page_action',views.edit_page_action),
]