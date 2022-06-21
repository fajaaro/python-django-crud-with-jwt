from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_or_store),
    path('<param_1>/', views.show_or_update),
]