from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^register/$',views.register,name="user_register"),
    url(r'^login/$',views.user_login,name="user_login"),
    # url(r'^logout/$',views.logout,name="user_logout"),
]