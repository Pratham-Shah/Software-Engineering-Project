from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('login/', views.login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path('dash/', views.dashboard, name="dash"),
    url(r'^chart/$', views.HomeView.as_view(), name='home'),
    url(r'^api/data/$', views.get_data, name='api-data'),
    url(r'^api/chart/data/$', views.ChartData.as_view()),
    url(r'^api/pichart/data/$', views.PieChartData.as_view()),
    path('counts/', views.PostList.as_view(), name='post'),
    path('',views.index,name='index'),
    url(r'^piechart/$', views.PieView.as_view(), name='home'),

]
