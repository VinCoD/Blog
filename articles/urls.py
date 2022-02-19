from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('articles/', views.articles_list, name="list"),
    path('articles/<slug>', views.article_detail, name="detail"),
]
