# dappx/urls.py
from django.conf.urls import url
from stocks import views
# SET THE NAMESPACE!
app_name = 'stocks'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^user_login/$',views.user_login,name='user_login'),
]
