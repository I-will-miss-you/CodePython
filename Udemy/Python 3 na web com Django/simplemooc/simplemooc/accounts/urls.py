from django.conf.urls import url
from django.contrib.auth.views import login 

urlpatterns = [
    url(r'^entrar/$', login, {'template_name': 'accounts/login.html'}, name='login'),
]