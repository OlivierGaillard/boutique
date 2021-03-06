"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from .views import ArticleCreateView, ArticleDetailView, upload_pic, ArticleFilteredView


app_name = 'inventory'


urlpatterns = [
    #url('articles/', ArticlesListView.as_view(), name='articles'),
    url('articles/', ArticleFilteredView.as_view(), name='articles'),
    url('article_create', ArticleCreateView.as_view(), name='article_create'),
    url(r'^article_detail/(?P<pk>[0-9]+)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^upload_pic/(?P<pk>[0-9]+)$', upload_pic, name='upload_pic'),
]

