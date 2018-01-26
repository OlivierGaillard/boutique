from django.conf.urls import url
#from django.urls import
from django.contrib.auth import views
from django.contrib.auth.views import logout
from .views import MyLoginView, ThanksView

app_name = 'accounts'

urlpatterns = [
    #path('accounts', include('django.contrib.auth.urls')),
    url('login/',  MyLoginView.as_view(), name='login'),
    url('thanks/', ThanksView.as_view(),  name='thanks'),
    url('logout/', logout, {'next_page': '/accounts/thanks/',  }, name='logout'),
    ]
