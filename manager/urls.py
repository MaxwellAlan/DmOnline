from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^signin/$',views.signin,name="signin"),
    url(r'^signup/$',views.signup,name="signup"),
    url(r'^home/$',views.manager_home,name="manager_home"),
    url(r'^signout/$',views.signout,name="sign_out"),
    url(r'^map/$',views.map,name="map"),
    url(r'^tables/$',views.tables,name="tables"),
    url(r'^maptest/$',views.map_test,name="map_test"),
    # url(r'^logout/$',views.logout,name="user_logout"),
]
