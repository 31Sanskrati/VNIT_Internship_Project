from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('success', views.success, name='success'),
    path('edit_account', views.edit_account, name='edit_account'),
    path('view_account', views.view_account, name='view_account'),
    path('delete_account', views.delete_account, name='delete_account'),
    path('recover_account', views.recover_account, name='recover_account')
]