from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list),
    path('(<slug>[\w-]+)/', views.article_detail),
]
