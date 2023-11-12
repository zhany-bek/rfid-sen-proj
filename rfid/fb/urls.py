from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reg-tag', views.register_tag, name='tag-reg'),
    path('reg-success', views.reg_success, name='success-page')
]

