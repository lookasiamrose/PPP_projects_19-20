from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    re_path(r'^user/(\w+)/$', views.dashboard, name='dashboard'),
    re_path(r'^access_offer/$', views.access_offer, name='access_offer' ),
    re_path(r'^add_offer/$', views.add_offer, name='add_offer'),
    re_path(r'^market/(\w+\s*)+/$', views.market, name='market'),
]