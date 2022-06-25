from django.urls import path
from .views import AnotherLogin, AnotherLogout, register_view

urlpatterns = [
    path('login/', AnotherLogin.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('logout/', AnotherLogout.as_view(), name='logout'),
]
