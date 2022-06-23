from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<user_id>/', views.show_or_update_or_delete),
]