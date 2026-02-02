from django.urls import path
from .import views

urlpatterns = [
    path('create/',views.create_short_url,name='create_short_url'),
    path('<str:short_code>/',views.redirect_short,name='redirect_short'),
    path('delete/<int:pk>/',views.delete,name='delete')
]
