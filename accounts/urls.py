from django.urls import path
from .import views
urlpatterns = [
    path('',views.register_views,name='register'),
    path('login/',views.login_views,name='login'),
    path('logout/',views.logout_views,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard')
]
